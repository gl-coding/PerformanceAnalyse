# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example/personInfo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example/personInfo.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x18\x65xample/personInfo.proto\"\x8d\x01\n\nPersonInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x11\n\twork_unit\x18\x03 \x01(\t\x12)\n\nclass_mate\x18\x04 \x03(\x0b\x32\x15.PersonInfo.ClassMate\x1a&\n\tClassMate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\rb\x06proto3'
)




_PERSONINFO_CLASSMATE = _descriptor.Descriptor(
  name='ClassMate',
  full_name='PersonInfo.ClassMate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PersonInfo.ClassMate.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='PersonInfo.ClassMate.age', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=170,
)

_PERSONINFO = _descriptor.Descriptor(
  name='PersonInfo',
  full_name='PersonInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PersonInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='PersonInfo.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='work_unit', full_name='PersonInfo.work_unit', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='class_mate', full_name='PersonInfo.class_mate', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PERSONINFO_CLASSMATE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=170,
)

_PERSONINFO_CLASSMATE.containing_type = _PERSONINFO
_PERSONINFO.fields_by_name['class_mate'].message_type = _PERSONINFO_CLASSMATE
DESCRIPTOR.message_types_by_name['PersonInfo'] = _PERSONINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PersonInfo = _reflection.GeneratedProtocolMessageType('PersonInfo', (_message.Message,), {

  'ClassMate' : _reflection.GeneratedProtocolMessageType('ClassMate', (_message.Message,), {
    'DESCRIPTOR' : _PERSONINFO_CLASSMATE,
    '__module__' : 'example.personInfo_pb2'
    # @@protoc_insertion_point(class_scope:PersonInfo.ClassMate)
    })
  ,
  'DESCRIPTOR' : _PERSONINFO,
  '__module__' : 'example.personInfo_pb2'
  # @@protoc_insertion_point(class_scope:PersonInfo)
  })
_sym_db.RegisterMessage(PersonInfo)
_sym_db.RegisterMessage(PersonInfo.ClassMate)


# @@protoc_insertion_point(module_scope)