# -*- coding: utf-8 -*-
import datetime
import http.client
import os
from unittest import TestCase, skip, skipIf
from uuid import uuid4

from grpc import StatusCode
from grpc._channel import _InactiveRpcError, _MultiThreadedRendezvous

from axonclient.client import AxonClient, AxonEvent
from axonclient.exceptions import OutOfRangeError
from axonclient.protos import dcb_pb2


class AxonClientCase(TestCase):
    host = "localhost"
    port = 8124

    def connect(self, host: str | None = None, port: int | None = None) -> AxonClient:
        return AxonClient(self.url(host=host, port=port))

    def url(self, host: str | None = None, port: int | None = None) -> str:
        return f"{host or self.host}:{port or self.port}"

    def test_axon_server_is_running(self) -> None:
        conn = http.client.HTTPConnection(self.url(port=8024))
        try:
            conn.request("GET", "/")
            r1 = conn.getresponse()
            self.assertEqual(r1.status, 200, "Axon Server not running?")
        finally:
            conn.close()


class TestAxonClientWithAggregatesAPI(AxonClientCase):
    def test_failing_to_connect_raises_exception(self) -> None:
        client = self.connect(port=81244444)
        aggregate_id = str(uuid4())
        with self.assertRaises(_MultiThreadedRendezvous):
            client.list_aggregate_events(aggregate_id, 0, False)

    def test_append_and_list_aggregate_events(self) -> None:
        client = self.connect()
        aggregate_id = str(uuid4())

        # Check there are zero events in the aggregate sequence.
        result = client.list_aggregate_events(aggregate_id, 0, False)
        self.assertEqual(len(result), 0)

        event_topic = "event topic"
        event_revision = "1"
        event_state = b"123456789"

        # Append a single event.
        client.append_event(
            AxonEvent(
                aggregate_identifier=aggregate_id,
                aggregate_sequence_number=0,
                aggregate_type="AggregateRoot",
                payload_type=event_topic,
                payload_revision=event_revision,
                payload_data=event_state,
                snapshot=False,
                meta_data={},
            )
        )

        # Check there is one event.
        result = client.list_aggregate_events(aggregate_id, 0, False)
        self.assertEqual(len(result), 1)

        # Fail to append event at same position.
        with self.assertRaises(OutOfRangeError) as context:
            client.append_event(
                AxonEvent(
                    aggregate_identifier=aggregate_id,
                    aggregate_sequence_number=0,
                    aggregate_type="AggregateRoot",
                    payload_type=event_topic,
                    payload_revision=event_revision,
                    payload_data=event_state,
                    snapshot=False,
                    meta_data={},
                )
            )
        self.assertIn("Invalid sequence number", context.exception.args[0])

        # Check there is still only one event in the aggregate sequence.
        result = client.list_aggregate_events(aggregate_id, 0, False)
        self.assertEqual(len(result), 1)

        stored_event = result[0]
        self.assertIsInstance(stored_event, AxonEvent)
        self.assertEqual(stored_event.aggregate_identifier, aggregate_id)
        self.assertEqual(stored_event.aggregate_sequence_number, 0)
        self.assertEqual(stored_event.payload_type, event_topic)
        self.assertEqual(stored_event.payload_revision, event_revision)
        self.assertEqual(stored_event.payload_data, event_state)

        # Append two more events.
        client.append_event(
            [
                AxonEvent(
                    aggregate_identifier=aggregate_id,
                    aggregate_sequence_number=1,
                    aggregate_type="AggregateRoot",
                    payload_type=event_topic,
                    payload_revision=event_revision,
                    payload_data=event_state,
                    snapshot=False,
                    meta_data={},
                ),
                AxonEvent(
                    aggregate_identifier=aggregate_id,
                    aggregate_sequence_number=2,
                    aggregate_type="AggregateRoot",
                    payload_type=event_topic,
                    payload_revision=event_revision,
                    payload_data=event_state,
                    snapshot=False,
                    meta_data={},
                ),
            ]
        )

        # Check there are three events in the aggregate sequence.
        result = client.list_aggregate_events(aggregate_id, 0, False)
        self.assertEqual(len(result), 3)

    def test_list_application_events(self) -> None:
        client = self.connect()

        # Get the next token.
        last_token = client.get_last_token()
        next_token = last_token + 1

        # Check listing returns zero events in the application sequence since the next token.
        result = client.list_events(tracking_token=next_token, number_of_permits=10)
        self.assertEqual(len(result), 0)

        event_topic = "eventtopic"
        event_revision = "1"
        event_state = b"123456789"
        aggregate_id = str(uuid4())

        # Append two events.
        client.append_event(
            [
                AxonEvent(
                    aggregate_identifier=aggregate_id,
                    aggregate_sequence_number=0,
                    aggregate_type="AggregateRoot",
                    payload_type=event_topic,
                    payload_revision=event_revision,
                    payload_data=event_state,
                ),
                AxonEvent(
                    aggregate_identifier=aggregate_id,
                    aggregate_sequence_number=1,
                    aggregate_type="AggregateRoot",
                    payload_type=event_topic,
                    payload_revision=event_revision,
                    payload_data=event_state,
                ),
            ]
        )

        # Check listing returns two AxonEvents in the application sequence since the next token.
        result = client.list_events(tracking_token=next_token, number_of_permits=10)
        for _, axon_event in result:
            assert isinstance(axon_event, AxonEvent), type(axon_event)

        self.assertEqual(len(result), 2, "There were %s events" % len(result))

    def test_benchmark_append_aggregate_events(self) -> None:
        # Connect to Axon Server.
        client = self.connect()

        event_topic = "event topic"
        event_revision = "1"
        event_state = b"123456789"

        # Append a single event.
        print()
        num_iters = int(os.environ.get("TEST_BENCHMARK_NUM_ITERS", 3))
        for i in range(num_iters):
            start = datetime.datetime.now()
            aggregate_id = str(uuid4())
            num_per_iter = 1000
            for j in range(num_per_iter):
                client.append_event(
                    AxonEvent(
                        aggregate_identifier=aggregate_id,
                        aggregate_sequence_number=j,
                        aggregate_type="AggregateRoot",
                        payload_type=event_topic,
                        payload_revision=event_revision,
                        payload_data=event_state,
                        snapshot=False,
                        meta_data={},
                    )
                )
            duration = datetime.datetime.now() - start
            rate = num_per_iter / duration.total_seconds()
            print(f"After {(i + 1) * num_per_iter:} events, rate: {rate:.0f} events/s")

    def test_append_and_list_snapshot_events(self) -> None:
        client = self.connect()
        aggregate_id = str(uuid4())

        event_topic = "eventtopic"
        event_revision = "1"
        event_state = b"123456789"
        # Append an event.
        aggregate_event = AxonEvent(
            aggregate_identifier=aggregate_id,
            aggregate_sequence_number=0,
            aggregate_type="AggregateRoot",
            payload_type=event_topic,
            payload_revision=event_revision,
            payload_data=event_state,
        )
        client.append_event([aggregate_event])

        # Check there are no snapshots for this aggregate.
        result = client.list_snapshot_events(aggregate_id)
        self.assertEqual(result, [])

        # Append a snapshot for this aggregate.
        snapshot_event = AxonEvent(
            aggregate_identifier=aggregate_id,
            aggregate_sequence_number=0,
            aggregate_type="AggregateRoot",
            payload_type="",
            payload_revision="1",
            payload_data=b"",
            snapshot=True,
        )
        client.append_snapshot(snapshot_event)

        # Check there is one snapshot for this aggregate.
        result = client.list_snapshot_events(aggregate_id)
        self.assertEqual(len(result), 1)

        stored_snapshot = result[0]
        self.assertIsInstance(stored_snapshot, AxonEvent)
        self.assertEqual(stored_snapshot.aggregate_sequence_number, 0)
        self.assertEqual(stored_snapshot.aggregate_identifier, aggregate_id)

        # Fail to append snapshot at same position.
        with self.assertRaises(_InactiveRpcError) as cm:
            client.append_snapshot(
                AxonEvent(
                    aggregate_identifier=aggregate_id,
                    aggregate_sequence_number=1,
                    aggregate_type="AggregateRoot",
                    payload_type="a",
                    payload_revision="1",
                    payload_data=b"",
                    snapshot=True,
                )
            )
        self.assertEqual(cm.exception.code(), StatusCode.OUT_OF_RANGE)
        self.assertEqual(
            cm.exception.details(),
            "[AXONIQ-2000] Invalid sequence number while storing snapshot. Highest"
            f" aggregate {aggregate_id} sequence number: 0, snapshot sequence 1.",
        )

        result = client.list_snapshot_events(aggregate_id)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], snapshot_event)

        # Check there is one events in the aggregate sequence.
        result = client.list_aggregate_events(aggregate_id, 0, False)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], aggregate_event)


class TestAxonClientWithDCBAPI(AxonClientCase):
    def test_dcb_append(self) -> None:
        client = self.connect()

        tag1 = self._generate_tag()
        client.dcb_append(
            events=[self._generate_tagged_event(tag1)],
            condition=dcb_pb2.ConsistencyCondition(
                consistency_marker=2,
                criterion=[
                    dcb_pb2.Criterion(
                        tags_and_names=dcb_pb2.TagsAndNamesCriterion(
                            name=["OrderCreated"],
                            tag=[tag1],
                        ),
                    )
                ],
            ),
        )

    def _generate_tagged_event(self, tag: dcb_pb2.Tag) -> dcb_pb2.TaggedEvent:
        return dcb_pb2.TaggedEvent(
            event=dcb_pb2.Event(
                identifier=str(uuid4()),
                timestamp=0,
                name="OrderCreated",
                version="1",
                payload=b"12345",
                metadata={},
            ),
            tag=[tag],
        )

    def _generate_tag(self) -> dcb_pb2.Tag:
        return dcb_pb2.Tag(key=b"foo" + str(uuid4()).encode(), value=b"bar")

    # @skip("Not benchmarking")
    def test_benchmark_dcb_append(self) -> None:
        client = self.connect()

        print()
        num_iters = int(os.environ.get("TEST_BENCHMARK_NUM_ITERS", 3))
        for i in range(num_iters):
            start = datetime.datetime.now()
            num_per_iter = 1000
            for j in range(num_per_iter):
                tag1 = self._generate_tag()
                client.dcb_append(
                    events=[self._generate_tagged_event(tag1)],
                    condition=dcb_pb2.ConsistencyCondition(
                        consistency_marker=0,
                        criterion=[
                            dcb_pb2.Criterion(
                                tags_and_names=dcb_pb2.TagsAndNamesCriterion(
                                    name=["OrderCreated"],
                                    tag=[tag1],
                                ),
                            )
                        ],
                    ),
                )
            duration = datetime.datetime.now() - start
            rate = num_per_iter / duration.total_seconds()
            print(f"After {(i + 1) * num_per_iter:} events, rate: {rate:.0f} events/s")
