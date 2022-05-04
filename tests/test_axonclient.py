# -*- coding: utf-8 -*-
import http.client
from unittest import TestCase
from uuid import uuid4

from grpc import StatusCode
from grpc._channel import _InactiveRpcError, _MultiThreadedRendezvous

from axonclient.client import DEFAULT_LOCAL_AXONSERVER_URI, AxonClient, AxonEvent
from axonclient.exceptions import OutOfRangeError


class TestAxonClient(TestCase):
    def test_axon_server_is_running(self) -> None:
        conn = http.client.HTTPConnection("localhost:8024")
        try:
            conn.request("GET", "/")
            r1 = conn.getresponse()
            self.assertEqual(r1.status, 200, "Axon Server not running?")
        finally:
            conn.close()

    def test_failing_to_connect_raises_exception(self) -> None:
        uri = "localhost:81244444"  # wrong port
        client = AxonClient(uri)
        aggregate_id = str(uuid4())
        with self.assertRaises(_MultiThreadedRendezvous):
            client.list_aggregate_events(aggregate_id, 0, False)

    def test_append_and_list_aggregate_events(self) -> None:
        # Connect to Axon Server.
        client = AxonClient(DEFAULT_LOCAL_AXONSERVER_URI)
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
        uri = "localhost:8124"
        client = AxonClient(uri)

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

    def test_append_and_list_snapshot_events(self) -> None:
        uri = "localhost:8124"
        client = AxonClient(uri)
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
