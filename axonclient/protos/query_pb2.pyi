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

class QueryProviderOutbound(google.protobuf.message.Message):
    """Message containing Query related instructions for Axon Server"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUBSCRIBE_FIELD_NUMBER: builtins.int
    UNSUBSCRIBE_FIELD_NUMBER: builtins.int
    FLOW_CONTROL_FIELD_NUMBER: builtins.int
    QUERY_RESPONSE_FIELD_NUMBER: builtins.int
    QUERY_COMPLETE_FIELD_NUMBER: builtins.int
    SUBSCRIPTION_QUERY_RESPONSE_FIELD_NUMBER: builtins.int
    ACK_FIELD_NUMBER: builtins.int
    INSTRUCTION_ID_FIELD_NUMBER: builtins.int
    @property
    def subscribe(self) -> global___QuerySubscription:
        """Registers a Query Handler with AxonServer"""
        pass
    @property
    def unsubscribe(self) -> global___QuerySubscription:
        """Unregisters a Query Handler with AxonServer"""
        pass
    @property
    def flow_control(self) -> axonclient.protos.common_pb2.FlowControl:
        """Grant permits to AxonServer to send a number of messages to the client"""
        pass
    @property
    def query_response(self) -> global___QueryResponse:
        """Sends a Response to a Query received via the inbound stream"""
        pass
    @property
    def query_complete(self) -> global___QueryComplete:
        """Indicator that all responses for Query have been sent"""
        pass
    @property
    def subscription_query_response(self) -> global___SubscriptionQueryResponse:
        """Sends a response for a Subscription Query that has been received via the inbound stream"""
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
        subscribe: typing.Optional[global___QuerySubscription] = ...,
        unsubscribe: typing.Optional[global___QuerySubscription] = ...,
        flow_control: typing.Optional[axonclient.protos.common_pb2.FlowControl] = ...,
        query_response: typing.Optional[global___QueryResponse] = ...,
        query_complete: typing.Optional[global___QueryComplete] = ...,
        subscription_query_response: typing.Optional[
            global___SubscriptionQueryResponse
        ] = ...,
        ack: typing.Optional[axonclient.protos.common_pb2.InstructionAck] = ...,
        instruction_id: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "ack",
            b"ack",
            "flow_control",
            b"flow_control",
            "query_complete",
            b"query_complete",
            "query_response",
            b"query_response",
            "request",
            b"request",
            "subscribe",
            b"subscribe",
            "subscription_query_response",
            b"subscription_query_response",
            "unsubscribe",
            b"unsubscribe",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "ack",
            b"ack",
            "flow_control",
            b"flow_control",
            "instruction_id",
            b"instruction_id",
            "query_complete",
            b"query_complete",
            "query_response",
            b"query_response",
            "request",
            b"request",
            "subscribe",
            b"subscribe",
            "subscription_query_response",
            b"subscription_query_response",
            "unsubscribe",
            b"unsubscribe",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["request", b"request"]
    ) -> typing.Optional[
        typing_extensions.Literal[
            "subscribe",
            "unsubscribe",
            "flow_control",
            "query_response",
            "query_complete",
            "subscription_query_response",
            "ack",
        ]
    ]: ...

global___QueryProviderOutbound = QueryProviderOutbound

class QueryProviderInbound(google.protobuf.message.Message):
    """Queries or Query related instructions from AxonServer for the connected application"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACK_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    SUBSCRIPTION_QUERY_REQUEST_FIELD_NUMBER: builtins.int
    INSTRUCTION_ID_FIELD_NUMBER: builtins.int
    @property
    def ack(self) -> axonclient.protos.common_pb2.InstructionAck:
        """Acknowledgement of previously sent instruction via outbound stream"""
        pass
    @property
    def query(self) -> global___QueryRequest:
        """Represents an incoming Query, for which this component is expected to provide a response"""
        pass
    @property
    def subscription_query_request(self) -> global___SubscriptionQueryRequest:
        """Represents an incoming Subscription Query, for which this component is expected to provide a response and updates"""
        pass
    instruction_id: typing.Text
    """Instruction identifier. If this identifier is set, this instruction will be acknowledged via outbound stream"""

    def __init__(
        self,
        *,
        ack: typing.Optional[axonclient.protos.common_pb2.InstructionAck] = ...,
        query: typing.Optional[global___QueryRequest] = ...,
        subscription_query_request: typing.Optional[
            global___SubscriptionQueryRequest
        ] = ...,
        instruction_id: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "ack",
            b"ack",
            "query",
            b"query",
            "request",
            b"request",
            "subscription_query_request",
            b"subscription_query_request",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "ack",
            b"ack",
            "instruction_id",
            b"instruction_id",
            "query",
            b"query",
            "request",
            b"request",
            "subscription_query_request",
            b"subscription_query_request",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["request", b"request"]
    ) -> typing.Optional[
        typing_extensions.Literal["ack", "query", "subscription_query_request"]
    ]: ...

global___QueryProviderInbound = QueryProviderInbound

class QueryComplete(google.protobuf.message.Message):
    """Message indicating that all available responses to an incoming Query have been provided."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MESSAGE_ID_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    message_id: typing.Text
    """A unique identifier for this message"""

    request_id: typing.Text
    """The identifier of the incoming query to complete"""

    def __init__(
        self,
        *,
        message_id: typing.Text = ...,
        request_id: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "message_id", b"message_id", "request_id", b"request_id"
        ],
    ) -> None: ...

global___QueryComplete = QueryComplete

class QueryRequest(google.protobuf.message.Message):
    """Message representing an incoming Query"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class MetaDataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> axonclient.protos.common_pb2.MetaDataValue: ...
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[axonclient.protos.common_pb2.MetaDataValue] = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    MESSAGE_IDENTIFIER_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    META_DATA_FIELD_NUMBER: builtins.int
    RESPONSE_TYPE_FIELD_NUMBER: builtins.int
    PROCESSING_INSTRUCTIONS_FIELD_NUMBER: builtins.int
    CLIENT_ID_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    message_identifier: typing.Text
    """The message ID of the incoming Query"""

    query: typing.Text
    """The name of the Query to execute"""

    timestamp: builtins.int
    """The timestamp of the Query creation"""

    @property
    def payload(self) -> axonclient.protos.common_pb2.SerializedObject:
        """A payload accompanying the Query"""
        pass
    @property
    def meta_data(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        typing.Text, axonclient.protos.common_pb2.MetaDataValue
    ]:
        """Meta Data providing contextual information of the Query"""
        pass
    @property
    def response_type(self) -> axonclient.protos.common_pb2.SerializedObject:
        """An object describing the expectations of the Response Type"""
        pass
    @property
    def processing_instructions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        axonclient.protos.common_pb2.ProcessingInstruction
    ]:
        """Any instructions for components Routing or Handling the Query"""
        pass
    client_id: typing.Text
    """The unique identifier of the client instance dispatching the query"""

    component_name: typing.Text
    """The Name of the Component dispatching the query"""

    def __init__(
        self,
        *,
        message_identifier: typing.Text = ...,
        query: typing.Text = ...,
        timestamp: builtins.int = ...,
        payload: typing.Optional[axonclient.protos.common_pb2.SerializedObject] = ...,
        meta_data: typing.Optional[
            typing.Mapping[typing.Text, axonclient.protos.common_pb2.MetaDataValue]
        ] = ...,
        response_type: typing.Optional[
            axonclient.protos.common_pb2.SerializedObject
        ] = ...,
        processing_instructions: typing.Optional[
            typing.Iterable[axonclient.protos.common_pb2.ProcessingInstruction]
        ] = ...,
        client_id: typing.Text = ...,
        component_name: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "payload", b"payload", "response_type", b"response_type"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "client_id",
            b"client_id",
            "component_name",
            b"component_name",
            "message_identifier",
            b"message_identifier",
            "meta_data",
            b"meta_data",
            "payload",
            b"payload",
            "processing_instructions",
            b"processing_instructions",
            "query",
            b"query",
            "response_type",
            b"response_type",
            "timestamp",
            b"timestamp",
        ],
    ) -> None: ...

global___QueryRequest = QueryRequest

class QueryResponse(google.protobuf.message.Message):
    """Message that represents the Response to a Query"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class MetaDataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> axonclient.protos.common_pb2.MetaDataValue: ...
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[axonclient.protos.common_pb2.MetaDataValue] = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    MESSAGE_IDENTIFIER_FIELD_NUMBER: builtins.int
    ERROR_CODE_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    META_DATA_FIELD_NUMBER: builtins.int
    PROCESSING_INSTRUCTIONS_FIELD_NUMBER: builtins.int
    REQUEST_IDENTIFIER_FIELD_NUMBER: builtins.int
    message_identifier: typing.Text
    """The unique identifier of the Response Message"""

    error_code: typing.Text
    """An Error Code identifying the type of error, if any"""

    @property
    def error_message(self) -> axonclient.protos.common_pb2.ErrorMessage:
        """A detailed description of the error, if any"""
        pass
    @property
    def payload(self) -> axonclient.protos.common_pb2.SerializedObject:
        """The Payload of the Response Message"""
        pass
    @property
    def meta_data(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        typing.Text, axonclient.protos.common_pb2.MetaDataValue
    ]:
        """Any Meta Data describing the context of the Response Message"""
        pass
    @property
    def processing_instructions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        axonclient.protos.common_pb2.ProcessingInstruction
    ]:
        """Any instructions for components Routing or Handling the Response Message"""
        pass
    request_identifier: typing.Text
    """The unique identifier of the Query to which this is a response"""

    def __init__(
        self,
        *,
        message_identifier: typing.Text = ...,
        error_code: typing.Text = ...,
        error_message: typing.Optional[axonclient.protos.common_pb2.ErrorMessage] = ...,
        payload: typing.Optional[axonclient.protos.common_pb2.SerializedObject] = ...,
        meta_data: typing.Optional[
            typing.Mapping[typing.Text, axonclient.protos.common_pb2.MetaDataValue]
        ] = ...,
        processing_instructions: typing.Optional[
            typing.Iterable[axonclient.protos.common_pb2.ProcessingInstruction]
        ] = ...,
        request_identifier: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "error_message", b"error_message", "payload", b"payload"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "error_code",
            b"error_code",
            "error_message",
            b"error_message",
            "message_identifier",
            b"message_identifier",
            "meta_data",
            b"meta_data",
            "payload",
            b"payload",
            "processing_instructions",
            b"processing_instructions",
            "request_identifier",
            b"request_identifier",
        ],
    ) -> None: ...

global___QueryResponse = QueryResponse

class SubscriptionQuery(google.protobuf.message.Message):
    """Message that represents a Subscription Query"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUBSCRIPTION_IDENTIFIER_FIELD_NUMBER: builtins.int
    NUMBER_OF_PERMITS_FIELD_NUMBER: builtins.int
    QUERY_REQUEST_FIELD_NUMBER: builtins.int
    UPDATE_RESPONSE_TYPE_FIELD_NUMBER: builtins.int
    subscription_identifier: typing.Text
    """A unique identifier for this subscription"""

    number_of_permits: builtins.int
    """The number of messages the Server may send before needing to await additional permits"""

    @property
    def query_request(self) -> global___QueryRequest:
        """The Query describing the desire for information"""
        pass
    @property
    def update_response_type(self) -> axonclient.protos.common_pb2.SerializedObject:
        """A description of the type of Object expected as Update Responses"""
        pass
    def __init__(
        self,
        *,
        subscription_identifier: typing.Text = ...,
        number_of_permits: builtins.int = ...,
        query_request: typing.Optional[global___QueryRequest] = ...,
        update_response_type: typing.Optional[
            axonclient.protos.common_pb2.SerializedObject
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "query_request",
            b"query_request",
            "update_response_type",
            b"update_response_type",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "number_of_permits",
            b"number_of_permits",
            "query_request",
            b"query_request",
            "subscription_identifier",
            b"subscription_identifier",
            "update_response_type",
            b"update_response_type",
        ],
    ) -> None: ...

global___SubscriptionQuery = SubscriptionQuery

class QueryUpdate(google.protobuf.message.Message):
    """A message containing an Update of a Query Subscription Response"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class MetaDataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        @property
        def value(self) -> axonclient.protos.common_pb2.MetaDataValue: ...
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[axonclient.protos.common_pb2.MetaDataValue] = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    MESSAGE_IDENTIFIER_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    META_DATA_FIELD_NUMBER: builtins.int
    CLIENT_ID_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    message_identifier: typing.Text
    """The unique identifier of this Update"""

    @property
    def payload(self) -> axonclient.protos.common_pb2.SerializedObject:
        """The object representing the Update"""
        pass
    @property
    def meta_data(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        typing.Text, axonclient.protos.common_pb2.MetaDataValue
    ]:
        """Meta Data providing contextual information of the Update"""
        pass
    client_id: typing.Text
    """The identifier of the Client instance providing the Update"""

    component_name: typing.Text
    """The Component Name of the Client providing the Update"""

    def __init__(
        self,
        *,
        message_identifier: typing.Text = ...,
        payload: typing.Optional[axonclient.protos.common_pb2.SerializedObject] = ...,
        meta_data: typing.Optional[
            typing.Mapping[typing.Text, axonclient.protos.common_pb2.MetaDataValue]
        ] = ...,
        client_id: typing.Text = ...,
        component_name: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["payload", b"payload"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "client_id",
            b"client_id",
            "component_name",
            b"component_name",
            "message_identifier",
            b"message_identifier",
            "meta_data",
            b"meta_data",
            "payload",
            b"payload",
        ],
    ) -> None: ...

global___QueryUpdate = QueryUpdate

class QueryUpdateComplete(google.protobuf.message.Message):
    """Message indicating that all relevant Updates have been sent for a Subscription Query, and that no further Updates are available"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLIENT_ID_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    client_id: typing.Text
    """The identifier of the Client instance providing the Update"""

    component_name: typing.Text
    """The Component Name of the Client providing the Update"""

    def __init__(
        self,
        *,
        client_id: typing.Text = ...,
        component_name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "client_id", b"client_id", "component_name", b"component_name"
        ],
    ) -> None: ...

global___QueryUpdateComplete = QueryUpdateComplete

class QueryUpdateCompleteExceptionally(google.protobuf.message.Message):
    """Message indicating that an Error occurred and that no Updates will be sent for a Subscription Query"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CLIENT_ID_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    ERROR_CODE_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    client_id: typing.Text
    """The identifier of the Client instance providing the Update"""

    component_name: typing.Text
    """The Component Name of the Client providing the Update"""

    error_code: typing.Text
    """The Code describing the type of Error that occurred"""

    @property
    def error_message(self) -> axonclient.protos.common_pb2.ErrorMessage:
        """A detailed description of the error, if available"""
        pass
    def __init__(
        self,
        *,
        client_id: typing.Text = ...,
        component_name: typing.Text = ...,
        error_code: typing.Text = ...,
        error_message: typing.Optional[axonclient.protos.common_pb2.ErrorMessage] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["error_message", b"error_message"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "client_id",
            b"client_id",
            "component_name",
            b"component_name",
            "error_code",
            b"error_code",
            "error_message",
            b"error_message",
        ],
    ) -> None: ...

global___QueryUpdateCompleteExceptionally = QueryUpdateCompleteExceptionally

class SubscriptionQueryRequest(google.protobuf.message.Message):
    """Message describing possible interactions for a Subscription Query"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SUBSCRIBE_FIELD_NUMBER: builtins.int
    UNSUBSCRIBE_FIELD_NUMBER: builtins.int
    GET_INITIAL_RESULT_FIELD_NUMBER: builtins.int
    FLOW_CONTROL_FIELD_NUMBER: builtins.int
    @property
    def subscribe(self) -> global___SubscriptionQuery:
        """Start a Subscription Query with the given details."""
        pass
    @property
    def unsubscribe(self) -> global___SubscriptionQuery:
        """Ends a previously started Subscription Query with the given details"""
        pass
    @property
    def get_initial_result(self) -> global___SubscriptionQuery:
        """Requests the initial result of a subscription query to be sent. This should always be done after opening the
        subscription query itself, to remove concurrency conflicts with Update messages.
        """
        pass
    @property
    def flow_control(self) -> global___SubscriptionQuery:
        """Allows the Server to provide additional Updates to be sent. Only the `number_of_permits` field needs to be
        set on this message.
        """
        pass
    def __init__(
        self,
        *,
        subscribe: typing.Optional[global___SubscriptionQuery] = ...,
        unsubscribe: typing.Optional[global___SubscriptionQuery] = ...,
        get_initial_result: typing.Optional[global___SubscriptionQuery] = ...,
        flow_control: typing.Optional[global___SubscriptionQuery] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "flow_control",
            b"flow_control",
            "get_initial_result",
            b"get_initial_result",
            "request",
            b"request",
            "subscribe",
            b"subscribe",
            "unsubscribe",
            b"unsubscribe",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "flow_control",
            b"flow_control",
            "get_initial_result",
            b"get_initial_result",
            "request",
            b"request",
            "subscribe",
            b"subscribe",
            "unsubscribe",
            b"unsubscribe",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["request", b"request"]
    ) -> typing.Optional[
        typing_extensions.Literal[
            "subscribe", "unsubscribe", "get_initial_result", "flow_control"
        ]
    ]: ...

global___SubscriptionQueryRequest = SubscriptionQueryRequest

class SubscriptionQueryResponse(google.protobuf.message.Message):
    """Represents a Response Message for a Subscription Query"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MESSAGE_IDENTIFIER_FIELD_NUMBER: builtins.int
    SUBSCRIPTION_IDENTIFIER_FIELD_NUMBER: builtins.int
    INITIAL_RESULT_FIELD_NUMBER: builtins.int
    UPDATE_FIELD_NUMBER: builtins.int
    COMPLETE_FIELD_NUMBER: builtins.int
    COMPLETE_EXCEPTIONALLY_FIELD_NUMBER: builtins.int
    message_identifier: typing.Text
    """The unique identifier for this message"""

    subscription_identifier: typing.Text
    """The identifier of the subscription query this is a response for"""

    @property
    def initial_result(self) -> global___QueryResponse:
        """Provides an Initial Response"""
        pass
    @property
    def update(self) -> global___QueryUpdate:
        """Provides an Update Response"""
        pass
    @property
    def complete(self) -> global___QueryUpdateComplete:
        """Indicates the Query is complete, and no more Updates will be sent"""
        pass
    @property
    def complete_exceptionally(self) -> global___QueryUpdateCompleteExceptionally:
        """Indicates the Query failed exceptionally, and no more Updates will be sent"""
        pass
    def __init__(
        self,
        *,
        message_identifier: typing.Text = ...,
        subscription_identifier: typing.Text = ...,
        initial_result: typing.Optional[global___QueryResponse] = ...,
        update: typing.Optional[global___QueryUpdate] = ...,
        complete: typing.Optional[global___QueryUpdateComplete] = ...,
        complete_exceptionally: typing.Optional[
            global___QueryUpdateCompleteExceptionally
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "complete",
            b"complete",
            "complete_exceptionally",
            b"complete_exceptionally",
            "initial_result",
            b"initial_result",
            "response",
            b"response",
            "update",
            b"update",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "complete",
            b"complete",
            "complete_exceptionally",
            b"complete_exceptionally",
            "initial_result",
            b"initial_result",
            "message_identifier",
            b"message_identifier",
            "response",
            b"response",
            "subscription_identifier",
            b"subscription_identifier",
            "update",
            b"update",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["response", b"response"]
    ) -> typing.Optional[
        typing_extensions.Literal[
            "initial_result", "update", "complete", "complete_exceptionally"
        ]
    ]: ...

global___SubscriptionQueryResponse = SubscriptionQueryResponse

class QuerySubscription(google.protobuf.message.Message):
    """Message containing details of a Registration of a Query Handler in a component"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MESSAGE_ID_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    RESULT_NAME_FIELD_NUMBER: builtins.int
    COMPONENT_NAME_FIELD_NUMBER: builtins.int
    CLIENT_ID_FIELD_NUMBER: builtins.int
    NR_OF_HANDLERS_FIELD_NUMBER: builtins.int
    message_id: typing.Text
    """The unique identifier of this Message"""

    query: typing.Text
    """The name of the Query the Handler is subscribed to"""

    result_name: typing.Text
    """The type of Result this Handler produces"""

    component_name: typing.Text
    """The name of the Component containing the Query Handler"""

    client_id: typing.Text
    """The unique identifier of the Client Instance containing the Query Handler"""

    nr_of_handlers: builtins.int
    """The number of Query Handlers registered within this Component with the same details. This number is used to
    calculate the number of candidates for Scatter-Gather Queries.
    """

    def __init__(
        self,
        *,
        message_id: typing.Text = ...,
        query: typing.Text = ...,
        result_name: typing.Text = ...,
        component_name: typing.Text = ...,
        client_id: typing.Text = ...,
        nr_of_handlers: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "client_id",
            b"client_id",
            "component_name",
            b"component_name",
            "message_id",
            b"message_id",
            "nr_of_handlers",
            b"nr_of_handlers",
            "query",
            b"query",
            "result_name",
            b"result_name",
        ],
    ) -> None: ...

global___QuerySubscription = QuerySubscription
