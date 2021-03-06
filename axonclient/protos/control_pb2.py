# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: axonclient/protos/control.proto
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
    b'\n\x1f\x61xonclient/protos/control.proto\x12!io.axoniq.axonserver.grpc.control\x1a\x1e\x61xonclient/protos/common.proto"\xe0\x02\n\x1aPlatformInboundInstruction\x12K\n\x08register\x18\x01'
    b" \x01(\x0b\x32\x37.io.axoniq.axonserver.grpc.control.ClientIdentificationH\x00\x12U\n\x14\x65vent_processor_info\x18\x02"
    b" \x01(\x0b\x32\x35.io.axoniq.axonserver.grpc.control.EventProcessorInfoH\x00\x12\x41\n\theartbeat\x18\x03"
    b" \x01(\x0b\x32,.io.axoniq.axonserver.grpc.control.HeartbeatH\x00\x12\x38\n\x03\x61\x63k\x18\x04"
    b" \x01(\x0b\x32).io.axoniq.axonserver.grpc.InstructionAckH\x00\x12\x16\n\x0einstruction_id\x18\x05"
    b' \x01(\tB\t\n\x07request"\xad\x07\n\x1bPlatformOutboundInstruction\x12H\n\x11node_notification\x18\x01'
    b" \x01(\x0b\x32+.io.axoniq.axonserver.grpc.control.NodeInfoH\x00\x12P\n\x11request_reconnect\x18\x03"
    b" \x01(\x0b\x32\x33.io.axoniq.axonserver.grpc.control.RequestReconnectH\x00\x12[\n\x15pause_event_processor\x18\x04"
    b" \x01(\x0b\x32:.io.axoniq.axonserver.grpc.control.EventProcessorReferenceH\x00\x12[\n\x15start_event_processor\x18\x05"
    b" \x01(\x0b\x32:.io.axoniq.axonserver.grpc.control.EventProcessorReferenceH\x00\x12\\\n\x0frelease_segment\x18\x06"
    b" \x01(\x0b\x32\x41.io.axoniq.axonserver.grpc.control.EventProcessorSegmentReferenceH\x00\x12\x62\n\x1crequest_event_processor_info\x18\x07"
    b" \x01(\x0b\x32:.io.axoniq.axonserver.grpc.control.EventProcessorReferenceH\x00\x12j\n\x1dsplit_event_processor_segment\x18\x08"
    b" \x01(\x0b\x32\x41.io.axoniq.axonserver.grpc.control.EventProcessorSegmentReferenceH\x00\x12j\n\x1dmerge_event_processor_segment\x18\t"
    b" \x01(\x0b\x32\x41.io.axoniq.axonserver.grpc.control.EventProcessorSegmentReferenceH\x00\x12\x41\n\theartbeat\x18\n"
    b" \x01(\x0b\x32,.io.axoniq.axonserver.grpc.control.HeartbeatH\x00\x12\x38\n\x03\x61\x63k\x18\x0b"
    b" \x01(\x0b\x32).io.axoniq.axonserver.grpc.InstructionAckH\x00\x12\x16\n\x0einstruction_id\x18\x0c"
    b' \x01(\tB\t\n\x07request"\x12\n\x10RequestReconnect"e\n\x0cPlatformInfo\x12<\n\x07primary\x18\x01'
    b" \x01(\x0b\x32+.io.axoniq.axonserver.grpc.control.NodeInfo\x12\x17\n\x0fsame_connection\x18\x02"
    b' \x01(\x08"g\n\x08NodeInfo\x12\x11\n\thost_name\x18\x01'
    b" \x01(\t\x12\x11\n\tgrpc_port\x18\x02 \x01(\x05\x12\x11\n\thttp_port\x18\x03"
    b" \x01(\x05\x12\x0f\n\x07version\x18\x04 \x01(\x05\x12\x11\n\tnode_name\x18\x05"
    b' \x01(\t"\xd0\x01\n\x14\x43lientIdentification\x12\x11\n\tclient_id\x18\x01'
    b" \x01(\t\x12\x16\n\x0e\x63omponent_name\x18\x02 \x01(\t\x12O\n\x04tags\x18\x03"
    b" \x03(\x0b\x32\x41.io.axoniq.axonserver.grpc.control.ClientIdentification.TagsEntry\x12\x0f\n\x07version\x18\x04"
    b" \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01"
    b" \x01(\t\x12\r\n\x05value\x18\x02"
    b' \x01(\t:\x02\x38\x01"\xf8\x02\n\x12\x45ventProcessorInfo\x12\x16\n\x0eprocessor_name\x18\x01'
    b" \x01(\t\x12\x0c\n\x04mode\x18\x02"
    b" \x01(\t\x12\x16\n\x0e\x61\x63tive_threads\x18\x03"
    b" \x01(\x05\x12\x0f\n\x07running\x18\x04 \x01(\x08\x12\r\n\x05\x65rror\x18\x05"
    b" \x01(\x08\x12[\n\x0esegment_status\x18\x06"
    b" \x03(\x0b\x32\x43.io.axoniq.axonserver.grpc.control.EventProcessorInfo.SegmentStatus\x12\x19\n\x11\x61vailable_threads\x18\x07"
    b" \x01(\x05\x1a\x8b\x01\n\rSegmentStatus\x12\x12\n\nsegment_id\x18\x01"
    b" \x01(\x05\x12\x11\n\tcaught_up\x18\x02 \x01(\x08\x12\x11\n\treplaying\x18\x03"
    b" \x01(\x08\x12\x13\n\x0bone_part_of\x18\x04"
    b" \x01(\x05\x12\x16\n\x0etoken_position\x18\x05"
    b" \x01(\x03\x12\x13\n\x0b\x65rror_state\x18\x06"
    b' \x01(\t"1\n\x17\x45ventProcessorReference\x12\x16\n\x0eprocessor_name\x18\x01'
    b' \x01(\t"T\n\x1e\x45ventProcessorSegmentReference\x12\x16\n\x0eprocessor_name\x18\x01'
    b" \x01(\t\x12\x1a\n\x12segment_identifier\x18\x02"
    b' \x01(\x05"\x0b\n\tHeartbeat2\xa6\x02\n\x0fPlatformService\x12\x7f\n\x11GetPlatformServer\x12\x37.io.axoniq.axonserver.grpc.control.ClientIdentification\x1a/.io.axoniq.axonserver.grpc.control.PlatformInfo"\x00\x12\x91\x01\n\nOpenStream\x12=.io.axoniq.axonserver.grpc.control.PlatformInboundInstruction\x1a>.io.axoniq.axonserver.grpc.control.PlatformOutboundInstruction"\x00(\x01\x30\x01\x42\x02P\x01\x62\x06proto3'
)


_PLATFORMINBOUNDINSTRUCTION = DESCRIPTOR.message_types_by_name[
    "PlatformInboundInstruction"
]
_PLATFORMOUTBOUNDINSTRUCTION = DESCRIPTOR.message_types_by_name[
    "PlatformOutboundInstruction"
]
_REQUESTRECONNECT = DESCRIPTOR.message_types_by_name["RequestReconnect"]
_PLATFORMINFO = DESCRIPTOR.message_types_by_name["PlatformInfo"]
_NODEINFO = DESCRIPTOR.message_types_by_name["NodeInfo"]
_CLIENTIDENTIFICATION = DESCRIPTOR.message_types_by_name["ClientIdentification"]
_CLIENTIDENTIFICATION_TAGSENTRY = _CLIENTIDENTIFICATION.nested_types_by_name[
    "TagsEntry"
]
_EVENTPROCESSORINFO = DESCRIPTOR.message_types_by_name["EventProcessorInfo"]
_EVENTPROCESSORINFO_SEGMENTSTATUS = _EVENTPROCESSORINFO.nested_types_by_name[
    "SegmentStatus"
]
_EVENTPROCESSORREFERENCE = DESCRIPTOR.message_types_by_name["EventProcessorReference"]
_EVENTPROCESSORSEGMENTREFERENCE = DESCRIPTOR.message_types_by_name[
    "EventProcessorSegmentReference"
]
_HEARTBEAT = DESCRIPTOR.message_types_by_name["Heartbeat"]
PlatformInboundInstruction = _reflection.GeneratedProtocolMessageType(
    "PlatformInboundInstruction",
    (_message.Message,),
    {
        "DESCRIPTOR": _PLATFORMINBOUNDINSTRUCTION,
        "__module__": "axonclient.protos.control_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.control.PlatformInboundInstruction)
    },
)
_sym_db.RegisterMessage(PlatformInboundInstruction)

PlatformOutboundInstruction = _reflection.GeneratedProtocolMessageType(
    "PlatformOutboundInstruction",
    (_message.Message,),
    {
        "DESCRIPTOR": _PLATFORMOUTBOUNDINSTRUCTION,
        "__module__": "axonclient.protos.control_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.control.PlatformOutboundInstruction)
    },
)
_sym_db.RegisterMessage(PlatformOutboundInstruction)

RequestReconnect = _reflection.GeneratedProtocolMessageType(
    "RequestReconnect",
    (_message.Message,),
    {
        "DESCRIPTOR": _REQUESTRECONNECT,
        "__module__": "axonclient.protos.control_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.control.RequestReconnect)
    },
)
_sym_db.RegisterMessage(RequestReconnect)

PlatformInfo = _reflection.GeneratedProtocolMessageType(
    "PlatformInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _PLATFORMINFO,
        "__module__": "axonclient.protos.control_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.control.PlatformInfo)
    },
)
_sym_db.RegisterMessage(PlatformInfo)

NodeInfo = _reflection.GeneratedProtocolMessageType(
    "NodeInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _NODEINFO,
        "__module__": "axonclient.protos.control_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.control.NodeInfo)
    },
)
_sym_db.RegisterMessage(NodeInfo)

ClientIdentification = _reflection.GeneratedProtocolMessageType(
    "ClientIdentification",
    (_message.Message,),
    {
        "TagsEntry": _reflection.GeneratedProtocolMessageType(
            "TagsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _CLIENTIDENTIFICATION_TAGSENTRY,
                "__module__": "axonclient.protos.control_pb2"
                # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.control.ClientIdentification.TagsEntry)
            },
        ),
        "DESCRIPTOR": _CLIENTIDENTIFICATION,
        "__module__": "axonclient.protos.control_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.control.ClientIdentification)
    },
)
_sym_db.RegisterMessage(ClientIdentification)
_sym_db.RegisterMessage(ClientIdentification.TagsEntry)

EventProcessorInfo = _reflection.GeneratedProtocolMessageType(
    "EventProcessorInfo",
    (_message.Message,),
    {
        "SegmentStatus": _reflection.GeneratedProtocolMessageType(
            "SegmentStatus",
            (_message.Message,),
            {
                "DESCRIPTOR": _EVENTPROCESSORINFO_SEGMENTSTATUS,
                "__module__": "axonclient.protos.control_pb2"
                # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.control.EventProcessorInfo.SegmentStatus)
            },
        ),
        "DESCRIPTOR": _EVENTPROCESSORINFO,
        "__module__": "axonclient.protos.control_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.control.EventProcessorInfo)
    },
)
_sym_db.RegisterMessage(EventProcessorInfo)
_sym_db.RegisterMessage(EventProcessorInfo.SegmentStatus)

EventProcessorReference = _reflection.GeneratedProtocolMessageType(
    "EventProcessorReference",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVENTPROCESSORREFERENCE,
        "__module__": "axonclient.protos.control_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.control.EventProcessorReference)
    },
)
_sym_db.RegisterMessage(EventProcessorReference)

EventProcessorSegmentReference = _reflection.GeneratedProtocolMessageType(
    "EventProcessorSegmentReference",
    (_message.Message,),
    {
        "DESCRIPTOR": _EVENTPROCESSORSEGMENTREFERENCE,
        "__module__": "axonclient.protos.control_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.control.EventProcessorSegmentReference)
    },
)
_sym_db.RegisterMessage(EventProcessorSegmentReference)

Heartbeat = _reflection.GeneratedProtocolMessageType(
    "Heartbeat",
    (_message.Message,),
    {
        "DESCRIPTOR": _HEARTBEAT,
        "__module__": "axonclient.protos.control_pb2"
        # @@protoc_insertion_point(class_scope:io.axoniq.axonserver.grpc.control.Heartbeat)
    },
)
_sym_db.RegisterMessage(Heartbeat)

_PLATFORMSERVICE = DESCRIPTOR.services_by_name["PlatformService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"P\001"
    _CLIENTIDENTIFICATION_TAGSENTRY._options = None
    _CLIENTIDENTIFICATION_TAGSENTRY._serialized_options = b"8\001"
    _PLATFORMINBOUNDINSTRUCTION._serialized_start = 103
    _PLATFORMINBOUNDINSTRUCTION._serialized_end = 455
    _PLATFORMOUTBOUNDINSTRUCTION._serialized_start = 458
    _PLATFORMOUTBOUNDINSTRUCTION._serialized_end = 1399
    _REQUESTRECONNECT._serialized_start = 1401
    _REQUESTRECONNECT._serialized_end = 1419
    _PLATFORMINFO._serialized_start = 1421
    _PLATFORMINFO._serialized_end = 1522
    _NODEINFO._serialized_start = 1524
    _NODEINFO._serialized_end = 1627
    _CLIENTIDENTIFICATION._serialized_start = 1630
    _CLIENTIDENTIFICATION._serialized_end = 1838
    _CLIENTIDENTIFICATION_TAGSENTRY._serialized_start = 1795
    _CLIENTIDENTIFICATION_TAGSENTRY._serialized_end = 1838
    _EVENTPROCESSORINFO._serialized_start = 1841
    _EVENTPROCESSORINFO._serialized_end = 2217
    _EVENTPROCESSORINFO_SEGMENTSTATUS._serialized_start = 2078
    _EVENTPROCESSORINFO_SEGMENTSTATUS._serialized_end = 2217
    _EVENTPROCESSORREFERENCE._serialized_start = 2219
    _EVENTPROCESSORREFERENCE._serialized_end = 2268
    _EVENTPROCESSORSEGMENTREFERENCE._serialized_start = 2270
    _EVENTPROCESSORSEGMENTREFERENCE._serialized_end = 2354
    _HEARTBEAT._serialized_start = 2356
    _HEARTBEAT._serialized_end = 2367
    _PLATFORMSERVICE._serialized_start = 2370
    _PLATFORMSERVICE._serialized_end = 2664
# @@protoc_insertion_point(module_scope)
