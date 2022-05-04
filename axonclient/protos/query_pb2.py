# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: axonclient/protos/query.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    descriptor_pool as _descriptor_pool,
    message as _message,
    reflection as _reflection,
    symbol_database as _symbol_database,
)

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from axonclient.protos import common_pb2 as axonclient_dot_protos_dot_common__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1d\x61xonclient/protos/query.proto\x12\x1fio.axoniq.axonserver.grpc.query\x1a\x1e\x61xonclient/protos/common.proto"\xbf\x04\n\x15QueryProviderOutbound\x12G\n\tsubscribe\x18\x01'
    b" \x01(\x0b\x32\x32.io.axoniq.axonserver.grpc.query.QuerySubscriptionH\x00\x12I\n\x0bunsubscribe\x18\x02"
    b" \x01(\x0b\x32\x32.io.axoniq.axonserver.grpc.query.QuerySubscriptionH\x00\x12>\n\x0c\x66low_control\x18\x03"
    b" \x01(\x0b\x32&.io.axoniq.axonserver.grpc.FlowControlH\x00\x12H\n\x0equery_response\x18\x04"
    b" \x01(\x0b\x32..io.axoniq.axonserver.grpc.query.QueryResponseH\x00\x12H\n\x0equery_complete\x18\x05"
    b" \x01(\x0b\x32..io.axoniq.axonserver.grpc.query.QueryCompleteH\x00\x12\x61\n\x1bsubscription_query_response\x18\x06"
    b" \x01(\x0b\x32:.io.axoniq.axonserver.grpc.query.SubscriptionQueryResponseH\x00\x12\x38\n\x03\x61\x63k\x18\x07"
    b" \x01(\x0b\x32).io.axoniq.axonserver.grpc.InstructionAckH\x00\x12\x16\n\x0einstruction_id\x18\x08"
    b' \x01(\tB\t\n\x07request"\x94\x02\n\x14QueryProviderInbound\x12\x38\n\x03\x61\x63k\x18\x01'
    b" \x01(\x0b\x32).io.axoniq.axonserver.grpc.InstructionAckH\x00\x12>\n\x05query\x18\x02"
    b" \x01(\x0b\x32-.io.axoniq.axonserver.grpc.query.QueryRequestH\x00\x12_\n\x1asubscription_query_request\x18\x03"
    b" \x01(\x0b\x32\x39.io.axoniq.axonserver.grpc.query.SubscriptionQueryRequestH\x00\x12\x16\n\x0einstruction_id\x18\x04"
    b' \x01(\tB\t\n\x07request"7\n\rQueryComplete\x12\x12\n\nmessage_id\x18\x01'
    b" \x01(\t\x12\x12\n\nrequest_id\x18\x02"
    b' \x01(\t"\xf7\x03\n\x0cQueryRequest\x12\x1a\n\x12message_identifier\x18\x01'
    b" \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03"
    b" \x01(\x03\x12<\n\x07payload\x18\x04"
    b" \x01(\x0b\x32+.io.axoniq.axonserver.grpc.SerializedObject\x12N\n\tmeta_data\x18\x05"
    b" \x03(\x0b\x32;.io.axoniq.axonserver.grpc.query.QueryRequest.MetaDataEntry\x12\x42\n\rresponse_type\x18\x06"
    b" \x01(\x0b\x32+.io.axoniq.axonserver.grpc.SerializedObject\x12Q\n\x17processing_instructions\x18\x07"
    b" \x03(\x0b\x32\x30.io.axoniq.axonserver.grpc.ProcessingInstruction\x12\x11\n\tclient_id\x18\x08"
    b" \x01(\t\x12\x16\n\x0e\x63omponent_name\x18\t"
    b" \x01(\t\x1aY\n\rMetaDataEntry\x12\x0b\n\x03key\x18\x01"
    b" \x01(\t\x12\x37\n\x05value\x18\x02"
    b' \x01(\x0b\x32(.io.axoniq.axonserver.grpc.MetaDataValue:\x02\x38\x01"\xde\x03\n\rQueryResponse\x12\x1a\n\x12message_identifier\x18\x01'
    b" \x01(\t\x12\x12\n\nerror_code\x18\x02 \x01(\t\x12>\n\rerror_message\x18\x03"
    b" \x01(\x0b\x32'.io.axoniq.axonserver.grpc.ErrorMessage\x12<\n\x07payload\x18\x04"
    b" \x01(\x0b\x32+.io.axoniq.axonserver.grpc.SerializedObject\x12O\n\tmeta_data\x18\x05"
    b" \x03(\x0b\x32<.io.axoniq.axonserver.grpc.query.QueryResponse.MetaDataEntry\x12Q\n\x17processing_instructions\x18\x06"
    b" \x03(\x0b\x32\x30.io.axoniq.axonserver.grpc.ProcessingInstruction\x12\x1a\n\x12request_identifier\x18\x07"
    b" \x01(\t\x1aY\n\rMetaDataEntry\x12\x0b\n\x03key\x18\x01"
    b" \x01(\t\x12\x37\n\x05value\x18\x02"
    b' \x01(\x0b\x32(.io.axoniq.axonserver.grpc.MetaDataValue:\x02\x38\x01J\x04\x08\x0f\x10\x10"\xe0\x01\n\x11SubscriptionQuery\x12\x1f\n\x17subscription_identifier\x18\x01'
    b" \x01(\t\x12\x19\n\x11number_of_permits\x18\x02"
    b" \x01(\x03\x12\x44\n\rquery_request\x18\x03"
    b" \x01(\x0b\x32-.io.axoniq.axonserver.grpc.query.QueryRequest\x12I\n\x14update_response_type\x18\x04"
    b' \x01(\x0b\x32+.io.axoniq.axonserver.grpc.SerializedObject"\xbc\x02\n\x0bQueryUpdate\x12\x1a\n\x12message_identifier\x18\x02'
    b" \x01(\t\x12<\n\x07payload\x18\x03"
    b" \x01(\x0b\x32+.io.axoniq.axonserver.grpc.SerializedObject\x12M\n\tmeta_data\x18\x04"
    b" \x03(\x0b\x32:.io.axoniq.axonserver.grpc.query.QueryUpdate.MetaDataEntry\x12\x11\n\tclient_id\x18\x05"
    b" \x01(\t\x12\x16\n\x0e\x63omponent_name\x18\x06"
    b" \x01(\t\x1aY\n\rMetaDataEntry\x12\x0b\n\x03key\x18\x01"
    b" \x01(\t\x12\x37\n\x05value\x18\x02"
    b' \x01(\x0b\x32(.io.axoniq.axonserver.grpc.MetaDataValue:\x02\x38\x01"@\n\x13QueryUpdateComplete\x12\x11\n\tclient_id\x18\x02'
    b' \x01(\t\x12\x16\n\x0e\x63omponent_name\x18\x03 \x01(\t"\xa1\x01\n'
    b" QueryUpdateCompleteExceptionally\x12\x11\n\tclient_id\x18\x02"
    b" \x01(\t\x12\x16\n\x0e\x63omponent_name\x18\x03"
    b" \x01(\t\x12\x12\n\nerror_code\x18\x05 \x01(\t\x12>\n\rerror_message\x18\x06"
    b" \x01(\x0b\x32'.io.axoniq.axonserver.grpc.ErrorMessage\"\xd7\x02\n\x18SubscriptionQueryRequest\x12G\n\tsubscribe\x18\x01"
    b" \x01(\x0b\x32\x32.io.axoniq.axonserver.grpc.query.SubscriptionQueryH\x00\x12I\n\x0bunsubscribe\x18\x02"
    b" \x01(\x0b\x32\x32.io.axoniq.axonserver.grpc.query.SubscriptionQueryH\x00\x12P\n\x12get_initial_result\x18\x03"
    b" \x01(\x0b\x32\x32.io.axoniq.axonserver.grpc.query.SubscriptionQueryH\x00\x12J\n\x0c\x66low_control\x18\x04"
    b' \x01(\x0b\x32\x32.io.axoniq.axonserver.grpc.query.SubscriptionQueryH\x00\x42\t\n\x07request"\x9d\x03\n\x19SubscriptionQueryResponse\x12\x1a\n\x12message_identifier\x18\x01'
    b" \x01(\t\x12\x1f\n\x17subscription_identifier\x18\x02"
    b" \x01(\t\x12H\n\x0einitial_result\x18\x03"
    b" \x01(\x0b\x32..io.axoniq.axonserver.grpc.query.QueryResponseH\x00\x12>\n\x06update\x18\x04"
    b" \x01(\x0b\x32,.io.axoniq.axonserver.grpc.query.QueryUpdateH\x00\x12H\n\x08\x63omplete\x18\x05"
    b" \x01(\x0b\x32\x34.io.axoniq.axonserver.grpc.query.QueryUpdateCompleteH\x00\x12\x63\n\x16\x63omplete_exceptionally\x18\x06"
    b' \x01(\x0b\x32\x41.io.axoniq.axonserver.grpc.query.QueryUpdateCompleteExceptionallyH\x00\x42\n\n\x08response"\x8e\x01\n\x11QuerySubscription\x12\x12\n\nmessage_id\x18\x01'
    b" \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\x12\x13\n\x0bresult_name\x18\x03"
    b" \x01(\t\x12\x16\n\x0e\x63omponent_name\x18\x04"
    b" \x01(\t\x12\x11\n\tclient_id\x18\x05 \x01(\t\x12\x16\n\x0enr_of_handlers\x18\x06"
    b' \x01(\x05\x32\x8c\x03\n\x0cQueryService\x12\x81\x01\n\nOpenStream\x12\x36.io.axoniq.axonserver.grpc.query.QueryProviderOutbound\x1a\x35.io.axoniq.axonserver.grpc.query.QueryProviderInbound"\x00(\x01\x30\x01\x12j\n\x05Query\x12-.io.axoniq.axonserver.grpc.query.QueryRequest\x1a..io.axoniq.axonserver.grpc.query.QueryResponse"\x00\x30\x01\x12\x8b\x01\n\x0cSubscription\x12\x39.io.axoniq.axonserver.grpc.query.SubscriptionQueryRequest\x1a:.io.axoniq.axonserver.grpc.query.SubscriptionQueryResponse"\x00(\x01\x30\x01\x42\x02P\x01\x62\x06proto3'
)


_QUERYPROVIDEROUTBOUND = DESCRIPTOR.message_types_by_name["QueryProviderOutbound"]
_QUERYPROVIDERINBOUND = DESCRIPTOR.message_types_by_name["QueryProviderInbound"]
_QUERYCOMPLETE = DESCRIPTOR.message_types_by_name["QueryComplete"]
_QUERYREQUEST = DESCRIPTOR.message_types_by_name["QueryRequest"]
_QUERYREQUEST_METADATAENTRY = _QUERYREQUEST.nested_types_by_name["MetaDataEntry"]
_QUERYRESPONSE = DESCRIPTOR.message_types_by_name["QueryResponse"]
_QUERYRESPONSE_METADATAENTRY = _QUERYRESPONSE.nested_types_by_name["MetaDataEntry"]
_SUBSCRIPTIONQUERY = DESCRIPTOR.message_types_by_name["SubscriptionQuery"]
_QUERYUPDATE = DESCRIPTOR.message_types_by_name["QueryUpdate"]
_QUERYUPDATE_METADATAENTRY = _QUERYUPDATE.nested_types_by_name["MetaDataEntry"]
_QUERYUPDATECOMPLETE = DESCRIPTOR.message_types_by_name["QueryUpdateComplete"]
_QUERYUPDATECOMPLETEEXCEPTIONALLY = DESCRIPTOR.message_types_by_name[
    "QueryUpdateCompleteExceptionally"
]
_SUBSCRIPTIONQUERYREQUEST = DESCRIPTOR.message_types_by_name["SubscriptionQueryRequest"]
_SUBSCRIPTIONQUERYRESPONSE = DESCRIPTOR.message_types_by_name[
    "SubscriptionQueryResponse"
]
_QUERYSUBSCRIPTION = DESCRIPTOR.message_types_by_name["QuerySubscription"]
QueryProviderOutbound = _reflection.GeneratedProtocolMessageType(
    "QueryProviderOutbound",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYPROVIDEROUTBOUND,
        "__module__": "axonclient.protos.query_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.QueryProviderOutbound)
    },
)
_sym_db.RegisterMessage(QueryProviderOutbound)

QueryProviderInbound = _reflection.GeneratedProtocolMessageType(
    "QueryProviderInbound",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYPROVIDERINBOUND,
        "__module__": "axonclient.protos.query_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.QueryProviderInbound)
    },
)
_sym_db.RegisterMessage(QueryProviderInbound)

QueryComplete = _reflection.GeneratedProtocolMessageType(
    "QueryComplete",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYCOMPLETE,
        "__module__": "axonclient.protos.query_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.QueryComplete)
    },
)
_sym_db.RegisterMessage(QueryComplete)

QueryRequest = _reflection.GeneratedProtocolMessageType(
    "QueryRequest",
    (_message.Message,),
    {
        "MetaDataEntry": _reflection.GeneratedProtocolMessageType(
            "MetaDataEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _QUERYREQUEST_METADATAENTRY,
                "__module__": "axonclient.protos.query_pb2"
                # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.QueryRequest.MetaDataEntry)
            },
        ),
        "DESCRIPTOR": _QUERYREQUEST,
        "__module__": "axonclient.protos.query_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.QueryRequest)
    },
)
_sym_db.RegisterMessage(QueryRequest)
_sym_db.RegisterMessage(QueryRequest.MetaDataEntry)

QueryResponse = _reflection.GeneratedProtocolMessageType(
    "QueryResponse",
    (_message.Message,),
    {
        "MetaDataEntry": _reflection.GeneratedProtocolMessageType(
            "MetaDataEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _QUERYRESPONSE_METADATAENTRY,
                "__module__": "axonclient.protos.query_pb2"
                # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.QueryResponse.MetaDataEntry)
            },
        ),
        "DESCRIPTOR": _QUERYRESPONSE,
        "__module__": "axonclient.protos.query_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.QueryResponse)
    },
)
_sym_db.RegisterMessage(QueryResponse)
_sym_db.RegisterMessage(QueryResponse.MetaDataEntry)

SubscriptionQuery = _reflection.GeneratedProtocolMessageType(
    "SubscriptionQuery",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUBSCRIPTIONQUERY,
        "__module__": "axonclient.protos.query_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.SubscriptionQuery)
    },
)
_sym_db.RegisterMessage(SubscriptionQuery)

QueryUpdate = _reflection.GeneratedProtocolMessageType(
    "QueryUpdate",
    (_message.Message,),
    {
        "MetaDataEntry": _reflection.GeneratedProtocolMessageType(
            "MetaDataEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _QUERYUPDATE_METADATAENTRY,
                "__module__": "axonclient.protos.query_pb2"
                # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.QueryUpdate.MetaDataEntry)
            },
        ),
        "DESCRIPTOR": _QUERYUPDATE,
        "__module__": "axonclient.protos.query_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.QueryUpdate)
    },
)
_sym_db.RegisterMessage(QueryUpdate)
_sym_db.RegisterMessage(QueryUpdate.MetaDataEntry)

QueryUpdateComplete = _reflection.GeneratedProtocolMessageType(
    "QueryUpdateComplete",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYUPDATECOMPLETE,
        "__module__": "axonclient.protos.query_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.QueryUpdateComplete)
    },
)
_sym_db.RegisterMessage(QueryUpdateComplete)

QueryUpdateCompleteExceptionally = _reflection.GeneratedProtocolMessageType(
    "QueryUpdateCompleteExceptionally",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYUPDATECOMPLETEEXCEPTIONALLY,
        "__module__": "axonclient.protos.query_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.QueryUpdateCompleteExceptionally)
    },
)
_sym_db.RegisterMessage(QueryUpdateCompleteExceptionally)

SubscriptionQueryRequest = _reflection.GeneratedProtocolMessageType(
    "SubscriptionQueryRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUBSCRIPTIONQUERYREQUEST,
        "__module__": "axonclient.protos.query_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.SubscriptionQueryRequest)
    },
)
_sym_db.RegisterMessage(SubscriptionQueryRequest)

SubscriptionQueryResponse = _reflection.GeneratedProtocolMessageType(
    "SubscriptionQueryResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUBSCRIPTIONQUERYRESPONSE,
        "__module__": "axonclient.protos.query_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.SubscriptionQueryResponse)
    },
)
_sym_db.RegisterMessage(SubscriptionQueryResponse)

QuerySubscription = _reflection.GeneratedProtocolMessageType(
    "QuerySubscription",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYSUBSCRIPTION,
        "__module__": "axonclient.protos.query_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.query.QuerySubscription)
    },
)
_sym_db.RegisterMessage(QuerySubscription)

_QUERYSERVICE = DESCRIPTOR.services_by_name["QueryService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"P\001"
    _QUERYREQUEST_METADATAENTRY._options = None
    _QUERYREQUEST_METADATAENTRY._serialized_options = b"8\001"
    _QUERYRESPONSE_METADATAENTRY._options = None
    _QUERYRESPONSE_METADATAENTRY._serialized_options = b"8\001"
    _QUERYUPDATE_METADATAENTRY._options = None
    _QUERYUPDATE_METADATAENTRY._serialized_options = b"8\001"
    _QUERYPROVIDEROUTBOUND._serialized_start = 99
    _QUERYPROVIDEROUTBOUND._serialized_end = 674
    _QUERYPROVIDERINBOUND._serialized_start = 677
    _QUERYPROVIDERINBOUND._serialized_end = 953
    _QUERYCOMPLETE._serialized_start = 955
    _QUERYCOMPLETE._serialized_end = 1010
    _QUERYREQUEST._serialized_start = 1013
    _QUERYREQUEST._serialized_end = 1516
    _QUERYREQUEST_METADATAENTRY._serialized_start = 1427
    _QUERYREQUEST_METADATAENTRY._serialized_end = 1516
    _QUERYRESPONSE._serialized_start = 1519
    _QUERYRESPONSE._serialized_end = 1997
    _QUERYRESPONSE_METADATAENTRY._serialized_start = 1427
    _QUERYRESPONSE_METADATAENTRY._serialized_end = 1516
    _SUBSCRIPTIONQUERY._serialized_start = 2000
    _SUBSCRIPTIONQUERY._serialized_end = 2224
    _QUERYUPDATE._serialized_start = 2227
    _QUERYUPDATE._serialized_end = 2543
    _QUERYUPDATE_METADATAENTRY._serialized_start = 1427
    _QUERYUPDATE_METADATAENTRY._serialized_end = 1516
    _QUERYUPDATECOMPLETE._serialized_start = 2545
    _QUERYUPDATECOMPLETE._serialized_end = 2609
    _QUERYUPDATECOMPLETEEXCEPTIONALLY._serialized_start = 2612
    _QUERYUPDATECOMPLETEEXCEPTIONALLY._serialized_end = 2773
    _SUBSCRIPTIONQUERYREQUEST._serialized_start = 2776
    _SUBSCRIPTIONQUERYREQUEST._serialized_end = 3119
    _SUBSCRIPTIONQUERYRESPONSE._serialized_start = 3122
    _SUBSCRIPTIONQUERYRESPONSE._serialized_end = 3535
    _QUERYSUBSCRIPTION._serialized_start = 3538
    _QUERYSUBSCRIPTION._serialized_end = 3680
    _QUERYSERVICE._serialized_start = 3683
    _QUERYSERVICE._serialized_end = 4079
# @@protoc_insertion_point(module_scope)
