# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/driver.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import node_pb2 as flwr_dot_proto_dot_node__pb2
from flwr.proto import task_pb2 as flwr_dot_proto_dot_task__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="flwr/proto/driver.proto",
    package="flwr.proto",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x17\x66lwr/proto/driver.proto\x12\nflwr.proto\x1a\x15\x66lwr/proto/node.proto\x1a\x15\x66lwr/proto/task.proto"\x11\n\x0fGetNodesRequest"$\n\x10GetNodesResponse\x12\x10\n\x08node_ids\x18\x01 \x03(\x04"@\n\x12PushTaskInsRequest\x12*\n\rtask_ins_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.TaskIns"\'\n\x13PushTaskInsResponse\x12\x10\n\x08task_ids\x18\x02 \x03(\t"F\n\x12PullTaskResRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12\x10\n\x08task_ids\x18\x02 \x03(\t"A\n\x13PullTaskResResponse\x12*\n\rtask_res_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.TaskRes2\xf5\x01\n\x06\x44river\x12G\n\x08GetNodes\x12\x1b.flwr.proto.GetNodesRequest\x1a\x1c.flwr.proto.GetNodesResponse"\x00\x12P\n\x0bPushTaskIns\x12\x1e.flwr.proto.PushTaskInsRequest\x1a\x1f.flwr.proto.PushTaskInsResponse"\x00\x12P\n\x0bPullTaskRes\x12\x1e.flwr.proto.PullTaskResRequest\x1a\x1f.flwr.proto.PullTaskResResponse"\x00\x62\x06proto3',
    dependencies=[
        flwr_dot_proto_dot_node__pb2.DESCRIPTOR,
        flwr_dot_proto_dot_task__pb2.DESCRIPTOR,
    ],
)


_GETNODESREQUEST = _descriptor.Descriptor(
    name="GetNodesRequest",
    full_name="flwr.proto.GetNodesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=85,
    serialized_end=102,
)


_GETNODESRESPONSE = _descriptor.Descriptor(
    name="GetNodesResponse",
    full_name="flwr.proto.GetNodesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="node_ids",
            full_name="flwr.proto.GetNodesResponse.node_ids",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=104,
    serialized_end=140,
)


_PUSHTASKINSREQUEST = _descriptor.Descriptor(
    name="PushTaskInsRequest",
    full_name="flwr.proto.PushTaskInsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="task_ins_list",
            full_name="flwr.proto.PushTaskInsRequest.task_ins_list",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=142,
    serialized_end=206,
)


_PUSHTASKINSRESPONSE = _descriptor.Descriptor(
    name="PushTaskInsResponse",
    full_name="flwr.proto.PushTaskInsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="task_ids",
            full_name="flwr.proto.PushTaskInsResponse.task_ids",
            index=0,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=208,
    serialized_end=247,
)


_PULLTASKRESREQUEST = _descriptor.Descriptor(
    name="PullTaskResRequest",
    full_name="flwr.proto.PullTaskResRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="node",
            full_name="flwr.proto.PullTaskResRequest.node",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="task_ids",
            full_name="flwr.proto.PullTaskResRequest.task_ids",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=249,
    serialized_end=319,
)


_PULLTASKRESRESPONSE = _descriptor.Descriptor(
    name="PullTaskResResponse",
    full_name="flwr.proto.PullTaskResResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="task_res_list",
            full_name="flwr.proto.PullTaskResResponse.task_res_list",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=321,
    serialized_end=386,
)

_PUSHTASKINSREQUEST.fields_by_name[
    "task_ins_list"
].message_type = flwr_dot_proto_dot_task__pb2._TASKINS
_PULLTASKRESREQUEST.fields_by_name[
    "node"
].message_type = flwr_dot_proto_dot_node__pb2._NODE
_PULLTASKRESRESPONSE.fields_by_name[
    "task_res_list"
].message_type = flwr_dot_proto_dot_task__pb2._TASKRES
DESCRIPTOR.message_types_by_name["GetNodesRequest"] = _GETNODESREQUEST
DESCRIPTOR.message_types_by_name["GetNodesResponse"] = _GETNODESRESPONSE
DESCRIPTOR.message_types_by_name["PushTaskInsRequest"] = _PUSHTASKINSREQUEST
DESCRIPTOR.message_types_by_name["PushTaskInsResponse"] = _PUSHTASKINSRESPONSE
DESCRIPTOR.message_types_by_name["PullTaskResRequest"] = _PULLTASKRESREQUEST
DESCRIPTOR.message_types_by_name["PullTaskResResponse"] = _PULLTASKRESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetNodesRequest = _reflection.GeneratedProtocolMessageType(
    "GetNodesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETNODESREQUEST,
        "__module__": "flwr.proto.driver_pb2"
        # @@protoc_insertion_point(class_scope:flwr.proto.GetNodesRequest)
    },
)
_sym_db.RegisterMessage(GetNodesRequest)

GetNodesResponse = _reflection.GeneratedProtocolMessageType(
    "GetNodesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETNODESRESPONSE,
        "__module__": "flwr.proto.driver_pb2"
        # @@protoc_insertion_point(class_scope:flwr.proto.GetNodesResponse)
    },
)
_sym_db.RegisterMessage(GetNodesResponse)

PushTaskInsRequest = _reflection.GeneratedProtocolMessageType(
    "PushTaskInsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _PUSHTASKINSREQUEST,
        "__module__": "flwr.proto.driver_pb2"
        # @@protoc_insertion_point(class_scope:flwr.proto.PushTaskInsRequest)
    },
)
_sym_db.RegisterMessage(PushTaskInsRequest)

PushTaskInsResponse = _reflection.GeneratedProtocolMessageType(
    "PushTaskInsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _PUSHTASKINSRESPONSE,
        "__module__": "flwr.proto.driver_pb2"
        # @@protoc_insertion_point(class_scope:flwr.proto.PushTaskInsResponse)
    },
)
_sym_db.RegisterMessage(PushTaskInsResponse)

PullTaskResRequest = _reflection.GeneratedProtocolMessageType(
    "PullTaskResRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _PULLTASKRESREQUEST,
        "__module__": "flwr.proto.driver_pb2"
        # @@protoc_insertion_point(class_scope:flwr.proto.PullTaskResRequest)
    },
)
_sym_db.RegisterMessage(PullTaskResRequest)

PullTaskResResponse = _reflection.GeneratedProtocolMessageType(
    "PullTaskResResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _PULLTASKRESRESPONSE,
        "__module__": "flwr.proto.driver_pb2"
        # @@protoc_insertion_point(class_scope:flwr.proto.PullTaskResResponse)
    },
)
_sym_db.RegisterMessage(PullTaskResResponse)


_DRIVER = _descriptor.ServiceDescriptor(
    name="Driver",
    full_name="flwr.proto.Driver",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=389,
    serialized_end=634,
    methods=[
        _descriptor.MethodDescriptor(
            name="GetNodes",
            full_name="flwr.proto.Driver.GetNodes",
            index=0,
            containing_service=None,
            input_type=_GETNODESREQUEST,
            output_type=_GETNODESRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="PushTaskIns",
            full_name="flwr.proto.Driver.PushTaskIns",
            index=1,
            containing_service=None,
            input_type=_PUSHTASKINSREQUEST,
            output_type=_PUSHTASKINSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="PullTaskRes",
            full_name="flwr.proto.Driver.PullTaskRes",
            index=2,
            containing_service=None,
            input_type=_PULLTASKRESREQUEST,
            output_type=_PULLTASKRESRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_DRIVER)

DESCRIPTOR.services_by_name["Driver"] = _DRIVER

# @@protoc_insertion_point(module_scope)
