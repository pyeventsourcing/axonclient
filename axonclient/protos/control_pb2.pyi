"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import axonclient.protos.common_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class PlatformInboundInstruction(google.protobuf.message.Message):
    """An instruction from Application Node to the AxonServer platform"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTER_FIELD_NUMBER: builtins.int
    EVENT_PROCESSOR_INFO_FIELD_NUMBER: builtins.int
    HEARTBEAT_FIELD_NUMBER: builtins.int
    ACK_FIELD_NUMBER: builtins.int
    INSTRUCTION_ID_FIELD_NUMBER: builtins.int
    @property
    def register(self) -> global___ClientIdentification:
        """Information about the client being connected.
        This information is used by AxonServer to monitor the topology of connected applications.
        """
        pass
    @property
    def event_processor_info(self) -> global___EventProcessorInfo:
        """Information about Tracking Processors defined in the application.
        This information is used by AxonServer to monitor the progress of Tracking Processors across instances.
        """
        pass
    @property
    def heartbeat(self) -> global___Heartbeat:
        """This heartbeat is used by AxonServer in order to check if the connection is still alive"""
        pass
    @property
    def ack(self) -> axonclient.protos.common_pb2.InstructionAck:
        """Acknowledgement of previously sent instruction via outbound stream"""
        pass
    instruction_id: typing.Text
    """Instruction identifier. If this identifier is set, this instruction will be acknowledged via outbound stream"""

    def __init__(
        self,
        *,
        register: typing.Optional[global___ClientIdentification] = ...,
        event_processor_info: typing.Optional[global___EventProcessorInfo] = ...,
        heartbeat: typing.Optional[global___Heartbeat] = ...,
        ack: typing.Optional[axonclient.protos.common_pb2.InstructionAck] = ...,
        instruction_id: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "ack",
            b"ack",
            "event_processor_info",
            b"event_processor_info",
            "heartbeat",
            b"heartbeat",
            "register",
            b"register",
            "request",
            b"request",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "ack",
            b"ack",
            "event_processor_info",
            b"event_processor_info",
            "heartbeat",
            b"heartbeat",
            "instruction_id",
            b"instruction_id",
            "register",
            b"register",
            "request",
            b"request",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["request", b"request"]
    ) -> typing.Optional[
        typing_extensions.Literal[
            "register", "event_processor_info", "heartbeat", "ack"
        ]
    ]: ...

global___PlatformInboundInstruction = PlatformInboundInstruction

class PlatformOutboundInstruction(google.protobuf.message.Message):
    """An instruction or information from the AxonServer Platform to the Application Node"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NODE_NOTIFICATION_FIELD_NUMBER: builtins.int
    REQUEST_RECONNECT_FIELD_NUMBER: builtins.int
    PAUSE_EVENT_PROCESSOR_FIELD_NUMBER: builtins.int
    START_EVENT_PROCESSOR_FIELD_NUMBER: builtins.int
    RELEASE_SEGMENT_FIELD_NUMBER: builtins.int
    REQUEST_EVENT_PROCESSOR_INFO_FIELD_NUMBER: builtins.int
    SPLIT_EVENT_PROCESSOR_SEGMENT_FIELD_NUMBER: builtins.int
    MERGE_EVENT_PROCESSOR_SEGMENT_FIELD_NUMBER: builtins.int
    HEARTBEAT_FIELD_NUMBER: builtins.int
    ACK_FIELD_NUMBER: builtins.int
    INSTRUCTION_ID_FIELD_NUMBER: builtins.int
    @property
    def node_notification(self) -> global___NodeInfo:
        """Information provided by AxonServer which provides information about the AxonServer node the application is connected with"""
        pass
    @property
    def request_reconnect(self) -> global___RequestReconnect:
        """A request from AxonServer to the Application to migrate its connection to another node.
        Clients SHOULD honor this request by closing their current connection, and using the GetPlatformServer RPC
        to request a new destination.
        """
        pass
    @property
    def pause_event_processor(self) -> global___EventProcessorReference:
        """Instruction from AxonServer to Pause a Tracking Event Processor."""
        pass
    @property
    def start_event_processor(self) -> global___EventProcessorReference:
        """Instruction from AxonServer to Start a Tracking Event Processor."""
        pass
    @property
    def release_segment(self) -> global___EventProcessorSegmentReference:
        """Instruction from AxonServer to Release a specific segment in a Tracking Event Processor"""
        pass
    @property
    def request_event_processor_info(self) -> global___EventProcessorReference:
        """A request from AxonServer for status information of a specific Tracking Event Processor"""
        pass
    @property
    def split_event_processor_segment(self) -> global___EventProcessorSegmentReference:
        """Instruction to split a Segment in a Tracking Event Processor"""
        pass
    @property
    def merge_event_processor_segment(self) -> global___EventProcessorSegmentReference:
        """Instruction to merge two Segments in a Tracking Event Processor"""
        pass
    @property
    def heartbeat(self) -> global___Heartbeat:
        """This heartbeat is used by AxonFramework in order to check if the connection is still alive"""
        pass
    @property
    def ack(self) -> axonclient.protos.common_pb2.InstructionAck:
        """Acknowledgement of previously sent instruction via inbound stream"""
        pass
    instruction_id: typing.Text
    """Instruction identifier. If this identifier is set, this instruction will be acknowledged via inbound stream"""

    def __init__(
        self,
        *,
        node_notification: typing.Optional[global___NodeInfo] = ...,
        request_reconnect: typing.Optional[global___RequestReconnect] = ...,
        pause_event_processor: typing.Optional[global___EventProcessorReference] = ...,
        start_event_processor: typing.Optional[global___EventProcessorReference] = ...,
        release_segment: typing.Optional[global___EventProcessorSegmentReference] = ...,
        request_event_processor_info: typing.Optional[
            global___EventProcessorReference
        ] = ...,
        split_event_processor_segment: typing.Optional[
            global___EventProcessorSegmentReference
        ] = ...,
        merge_event_processor_segment: typing.Optional[
            global___EventProcessorSegmentReference
        ] = ...,
        heartbeat: typing.Optional[global___Heartbeat] = ...,
        ack: typing.Optional[axonclient.protos.common_pb2.InstructionAck] = ...,
        instruction_id: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "ack",
            b"ack",
            "heartbeat",
            b"heartbeat",
            "merge_event_processor_segment",
            b"merge_event_processor_segment",
            "node_notification",
            b"node_notification",
            "pause_event_processor",
            b"pause_event_processor",
            "release_segment",
            b"release_segment",
            "request",
            b"request",
            "request_event_processor_info",
            b"request_event_processor_info",
            "request_reconnect",
            b"request_reconnect",
            "split_event_processor_segment",
            b"split_event_processor_segment",
            "start_event_processor",
            b"start_event_processor",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "ack",
            b"ack",
            "heartbeat",
            b"heartbeat",
            "instruction_id",
            b"instruction_id",
            "merge_event_processor_segment",
            b"merge_event_processor_segment",
            "node_notification",
            b"node_notification",
            "pause_event_processor",
            b"pause_event_processor",
            "release_segment",
            b"release_segment",
            "request",
            b"request",
            "request_event_processor_info",
            b"request_event_processor_info",
            "request_reconnect",
            b"request_reconnect",
            "split_event_processor_segment",
            b"split_event_processor_segment",
            "start_event_processor",
            b"start_event_processor",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["request", b"request"]
    ) -> typing.Optional[
        typing_extensions.Literal[
            "node_notification",
            "request_reconnect",
            "pause_event_processor",
            "start_event_processor",
            "release_segment",
            "request_event_processor_info",
            "split_event_processor_segment",
            "merge_event_processor_segment",
            "heartbeat",
            "ack",
        ]
    ]: ...

global___PlatformOutboundInstruction = PlatformOutboundInstruction

class RequestReconnect(google.protobuf.message.Message):
    """Message send when AxonServer requests the client to re-establish its connection with the Platform"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(
        self,
    ) -> None: ...

global___RequestReconnect = RequestReconnect

class PlatformInfo(google.protobuf.message.Message):
    """Message containing connection information of the node to Connect with"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PRIMARY_FIELD_NUMBER: builtins.int
    SAME_CONNECTION_FIELD_NUMBER: builtins.int
    @property
    def primary(self) -> global___NodeInfo:
        """The connection details of the node the client should connect with"""
        pass
    same_connection: builtins.bool
    """Flag indicating that the connection may be reused to connect. When true, the client _may_ reuse the connection
    established for the GetPlatformServer request for subsequent requests.
    """

    def __init__(
        self,
        *,
        primary: typing.Optional[global___NodeInfo] = ...,
        same_connection: builtins.bool = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["primary", b"primary"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "primary", b"primary", "same_connection", b"same_connection"
        ],
    ) -> None: ...

global___PlatformInfo = PlatformInfo

class NodeInfo(google.protobuf.message.Message):
    """Message containing connection information for an AxonServer Node"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HOST_NAME_FIELD_NUMBER: builtins.int
    GRPC_PORT_FIELD_NUMBER: builtins.int
    HTTP_PORT_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    NODE_NAME_FIELD_NUMBER: builtins.int
    host_name: typing.Text
    """The host name to use when connecting to this node"""

    grpc_port: builtins.int
    """The port number for gRPC connections"""

    http_port: builtins.int
    """The port number for HTTP connections"""

    version: builtins.int
    """The version identifier of the API"""

    node_name: typing.Text
    """The unique name of the node to connect with, for purpose of debugging"""

    def __init__(
        self,
        *,
        host_name: typing.Text = ...,
        grpc_port: builtins.int = ...,
        http_port: builtins.int = ...,
        version: builtins.int = ...,
        node_name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "grpc_port",
            b"grpc_port",
            "host_name",
            b"host_name",
            "http_port",
            b"http_port",
            "node_name",
            b"node_name",
            "version",
            b"version",
        ],
    ) -> None: ...

global___NodeInfo = NodeInfo

class ClientIdentification(google.protobuf.message.Message):
    """Message containing details about the Client Application"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class TagsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    CLIENT_ID_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    client_id: typing.Text
    """A unique identifier for this client instance. Is used to distinguish different instances of the same component"""

    component_name: typing.Text
    """The name of the component. Several instances of the same component should share this name"""

    @property
    def tags(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """Any tags associated with the client, which may provide hints and preferences for setting up connections"""
        pass
    version: typing.Text
    """Axon framework version used by the client application instance"""

    def __init__(
        self,
        *,
        client_id: typing.Text = ...,
        component_name: typing.Text = ...,
        tags: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        version: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "client_id",
            b"client_id",
            "component_name",
            b"component_name",
            "tags",
            b"tags",
            "version",
            b"version",
        ],
    ) -> None: ...

global___ClientIdentification = ClientIdentification

class EventProcessorInfo(google.protobuf.message.Message):
    """Message containing information about the status of a Tracking Event Processor"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class SegmentStatus(google.protobuf.message.Message):
        """Message containing information about the status of a Segment of a Tracking Event Processor"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        SEGMENT_ID_FIELD_NUMBER: builtins.int
        CAUGHT_UP_FIELD_NUMBER: builtins.int
        REPLAYING_FIELD_NUMBER: builtins.int
        ONE_PART_OF_FIELD_NUMBER: builtins.int
        TOKEN_POSITION_FIELD_NUMBER: builtins.int
        ERROR_STATE_FIELD_NUMBER: builtins.int
        segment_id: builtins.int
        """The ID of the Segment for which the status is reported"""

        caught_up: builtins.bool
        """Indicates whether the Segment has "Caught Up" with the Head of the Event Stream"""

        replaying: builtins.bool
        """Indicates whether the Segment is "Replaying" historic events after a Reset."""

        one_part_of: builtins.int
        """The fraction this segment processes. A fraction of 2 means 1/2, 4 means 1/4, etc."""

        token_position: builtins.int
        """The approximate position of the token in the stream."""

        error_state: typing.Text
        """Information about the error state of the Segment, if applicable."""

        def __init__(
            self,
            *,
            segment_id: builtins.int = ...,
            caught_up: builtins.bool = ...,
            replaying: builtins.bool = ...,
            one_part_of: builtins.int = ...,
            token_position: builtins.int = ...,
            error_state: typing.Text = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "caught_up",
                b"caught_up",
                "error_state",
                b"error_state",
                "one_part_of",
                b"one_part_of",
                "replaying",
                b"replaying",
                "segment_id",
                b"segment_id",
                "token_position",
                b"token_position",
            ],
        ) -> None: ...

    PROCESSOR_NAME_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    ACTIVE_THREADS_FIELD_NUMBER: builtins.int
    RUNNING_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    SEGMENT_STATUS_FIELD_NUMBER: builtins.int
    AVAILABLE_THREADS_FIELD_NUMBER: builtins.int
    processor_name: typing.Text
    """The logical name of this processor."""

    mode: typing.Text
    """The mode in which this processor is reading Events, for example: 'Tracking' or 'Subscribing'"""

    active_threads: builtins.int
    """The number of threads currently actively processing Events"""

    running: builtins.bool
    """Flag indicating whether the processor is running"""

    error: builtins.bool
    """Flag indicating whether the processor, when stopped, did so because of an irrecoverable Error"""

    @property
    def segment_status(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___EventProcessorInfo.SegmentStatus
    ]:
        """Status details of each of the Segments for which Events are being processed. This is only provided by Tracking
        Event Processors.
        """
        pass
    available_threads: builtins.int
    """The number of threads the processor has available to assign to Segments.
    Will report 0 if all threads are assigned a Segment.
    """

    def __init__(
        self,
        *,
        processor_name: typing.Text = ...,
        mode: typing.Text = ...,
        active_threads: builtins.int = ...,
        running: builtins.bool = ...,
        error: builtins.bool = ...,
        segment_status: typing.Optional[
            typing.Iterable[global___EventProcessorInfo.SegmentStatus]
        ] = ...,
        available_threads: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "active_threads",
            b"active_threads",
            "available_threads",
            b"available_threads",
            "error",
            b"error",
            "mode",
            b"mode",
            "processor_name",
            b"processor_name",
            "running",
            b"running",
            "segment_status",
            b"segment_status",
        ],
    ) -> None: ...

global___EventProcessorInfo = EventProcessorInfo

class EventProcessorReference(google.protobuf.message.Message):
    """Message providing reference to an Event Processor"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROCESSOR_NAME_FIELD_NUMBER: builtins.int
    processor_name: typing.Text
    """The name of the Event Processor"""

    def __init__(
        self,
        *,
        processor_name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["processor_name", b"processor_name"]
    ) -> None: ...

global___EventProcessorReference = EventProcessorReference

class EventProcessorSegmentReference(google.protobuf.message.Message):
    """Message providing reference to a Segment of an Event Processor"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROCESSOR_NAME_FIELD_NUMBER: builtins.int
    SEGMENT_IDENTIFIER_FIELD_NUMBER: builtins.int
    processor_name: typing.Text
    """The name of the Event Processor"""

    segment_identifier: builtins.int
    """The identifier of the Segment"""

    def __init__(
        self,
        *,
        processor_name: typing.Text = ...,
        segment_identifier: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "processor_name",
            b"processor_name",
            "segment_identifier",
            b"segment_identifier",
        ],
    ) -> None: ...

global___EventProcessorSegmentReference = EventProcessorSegmentReference

class Heartbeat(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(
        self,
    ) -> None: ...

global___Heartbeat = Heartbeat
