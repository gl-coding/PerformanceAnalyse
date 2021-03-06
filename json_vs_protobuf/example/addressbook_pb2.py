# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example/addressbook.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example/addressbook.proto',
  package='example',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x19\x65xample/addressbook.proto\x12\x07\x65xample\".\n\x0b\x41\x64\x64ressBook\x12\x1f\n\x06people\x18\x01 \x03(\x0b\x32\x0f.example.Person\"\x9d\x01\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\r\n\x05money\x18\x04 \x01(\x02\x12\x13\n\x0bwork_status\x18\x05 \x01(\x08\x12$\n\x06phones\x18\x06 \x03(\x0b\x32\x14.example.PhoneNumber\x12 \n\x04maps\x18\x07 \x01(\x0b\x32\x12.example.MyMessage\"?\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x01(\t\x12 \n\x04type\x18\x02 \x01(\x0e\x32\x12.example.PhoneType\"p\n\tMyMessage\x12\x32\n\x08mapfield\x18\x01 \x03(\x0b\x32 .example.MyMessage.MapfieldEntry\x1a/\n\rMapfieldEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01*+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\x62\x06proto3'
)

_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  full_name='example.PhoneType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=425,
  serialized_end=468,
)
_sym_db.RegisterEnumDescriptor(_PHONETYPE)

PhoneType = enum_type_wrapper.EnumTypeWrapper(_PHONETYPE)
MOBILE = 0
HOME = 1
WORK = 2



_ADDRESSBOOK = _descriptor.Descriptor(
  name='AddressBook',
  full_name='example.AddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='people', full_name='example.AddressBook.people', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=38,
  serialized_end=84,
)


_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='example.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='example.Person.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='example.Person.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='example.Person.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='money', full_name='example.Person.money', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='work_status', full_name='example.Person.work_status', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phones', full_name='example.Person.phones', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maps', full_name='example.Person.maps', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=87,
  serialized_end=244,
)


_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='example.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='example.PhoneNumber.number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='example.PhoneNumber.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=246,
  serialized_end=309,
)


_MYMESSAGE_MAPFIELDENTRY = _descriptor.Descriptor(
  name='MapfieldEntry',
  full_name='example.MyMessage.MapfieldEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='example.MyMessage.MapfieldEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='example.MyMessage.MapfieldEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=376,
  serialized_end=423,
)

_MYMESSAGE = _descriptor.Descriptor(
  name='MyMessage',
  full_name='example.MyMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mapfield', full_name='example.MyMessage.mapfield', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MYMESSAGE_MAPFIELDENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=423,
)

_ADDRESSBOOK.fields_by_name['people'].message_type = _PERSON
_PERSON.fields_by_name['phones'].message_type = _PHONENUMBER
_PERSON.fields_by_name['maps'].message_type = _MYMESSAGE
_PHONENUMBER.fields_by_name['type'].enum_type = _PHONETYPE
_MYMESSAGE_MAPFIELDENTRY.containing_type = _MYMESSAGE
_MYMESSAGE.fields_by_name['mapfield'].message_type = _MYMESSAGE_MAPFIELDENTRY
DESCRIPTOR.message_types_by_name['AddressBook'] = _ADDRESSBOOK
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['PhoneNumber'] = _PHONENUMBER
DESCRIPTOR.message_types_by_name['MyMessage'] = _MYMESSAGE
DESCRIPTOR.enum_types_by_name['PhoneType'] = _PHONETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESSBOOK,
  '__module__' : 'example.addressbook_pb2'
  # @@protoc_insertion_point(class_scope:example.AddressBook)
  })
_sym_db.RegisterMessage(AddressBook)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'example.addressbook_pb2'
  # @@protoc_insertion_point(class_scope:example.Person)
  })
_sym_db.RegisterMessage(Person)

PhoneNumber = _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), {
  'DESCRIPTOR' : _PHONENUMBER,
  '__module__' : 'example.addressbook_pb2'
  # @@protoc_insertion_point(class_scope:example.PhoneNumber)
  })
_sym_db.RegisterMessage(PhoneNumber)

MyMessage = _reflection.GeneratedProtocolMessageType('MyMessage', (_message.Message,), {

  'MapfieldEntry' : _reflection.GeneratedProtocolMessageType('MapfieldEntry', (_message.Message,), {
    'DESCRIPTOR' : _MYMESSAGE_MAPFIELDENTRY,
    '__module__' : 'example.addressbook_pb2'
    # @@protoc_insertion_point(class_scope:example.MyMessage.MapfieldEntry)
    })
  ,
  'DESCRIPTOR' : _MYMESSAGE,
  '__module__' : 'example.addressbook_pb2'
  # @@protoc_insertion_point(class_scope:example.MyMessage)
  })
_sym_db.RegisterMessage(MyMessage)
_sym_db.RegisterMessage(MyMessage.MapfieldEntry)


_MYMESSAGE_MAPFIELDENTRY._options = None
# @@protoc_insertion_point(module_scope)
