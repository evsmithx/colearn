# ------------------------------------------------------------------------------
#
#   Copyright 2021 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: interface.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='interface.proto',
  package='contract_learn.grpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0finterface.proto\x12\x13\x63ontract_learn.grpc\x1a\x1bgoogle/protobuf/empty.proto\"\x83\x01\n\x0eRequestMLSetup\x12\x1b\n\x13\x64\x61taset_loader_name\x18\x01 \x01(\t\x12!\n\x19\x64\x61taset_loader_parameters\x18\x02 \x01(\t\x12\x17\n\x0fmodel_arch_name\x18\x03 \x01(\t\x12\x18\n\x10model_parameters\x18\x04 \x01(\t\"Z\n\x0fResponseMLSetup\x12\x32\n\x06status\x18\x01 \x01(\x0e\x32\".contract_learn.grpc.MLSetupStatus\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x1a\n\x07Weights\x12\x0f\n\x07weights\x18\x01 \x01(\x0c\"\x89\x02\n\x0fProposedWeights\x12-\n\x07weights\x18\x01 \x01(\x0b\x32\x1c.contract_learn.grpc.Weights\x12\x12\n\nvote_score\x18\x02 \x01(\x02\x12\x12\n\ntest_score\x18\x03 \x01(\x02\x12\x0c\n\x04vote\x18\x04 \x01(\x08\x12W\n\x12\x65valuation_results\x18\x05 \x03(\x0b\x32;.contract_learn.grpc.ProposedWeights.EvaluationResultsEntry\x1a\x38\n\x16\x45valuationResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"\x0f\n\rRequestStatus\"C\n\x0eResponseStatus\x12\x31\n\x06status\x18\x01 \x01(\x0e\x32!.contract_learn.grpc.SystemStatus\"=\n\x11\x44\x61tasetLoaderSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x12\x64\x65\x66\x61ult_parameters\x18\x02 \x01(\t\"9\n\rModelArchSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x12\x64\x65\x66\x61ult_parameters\x18\x02 \x01(\t\"\xa6\x02\n\x17ResponseSupportedSystem\x12<\n\x0c\x64\x61ta_loaders\x18\x01 \x03(\x0b\x32&.contract_learn.grpc.DatasetLoaderSpec\x12?\n\x13model_architectures\x18\x02 \x03(\x0b\x32\".contract_learn.grpc.ModelArchSpec\x12V\n\rcompatibility\x18\x03 \x03(\x0b\x32?.contract_learn.grpc.ResponseSupportedSystem.CompatibilityEntry\x1a\x34\n\x12\x43ompatibilityEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01*6\n\rMLSetupStatus\x12\r\n\tUNDEFINED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02*J\n\x0cSystemStatus\x12\x0b\n\x07WORKING\x10\x00\x12\x0c\n\x08NO_MODEL\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x0b\n\x07UNKNOWN\x10\x03\x32\xff\x03\n\x0bGRPCLearner\x12\\\n\x14QuerySupportedSystem\x12\x16.google.protobuf.Empty\x1a,.contract_learn.grpc.ResponseSupportedSystem\x12T\n\x07MLSetup\x12#.contract_learn.grpc.RequestMLSetup\x1a$.contract_learn.grpc.ResponseMLSetup\x12H\n\x0eProposeWeights\x12\x16.google.protobuf.Empty\x1a\x1c.contract_learn.grpc.Weights0\x01\x12Q\n\x0bTestWeights\x12\x1c.contract_learn.grpc.Weights\x1a$.contract_learn.grpc.ProposedWeights\x12\x42\n\nSetWeights\x12\x1c.contract_learn.grpc.Weights\x1a\x16.google.protobuf.Empty\x12[\n\x0cStatusStream\x12\".contract_learn.grpc.RequestStatus\x1a#.contract_learn.grpc.ResponseStatus(\x01\x30\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_MLSETUPSTATUS = _descriptor.EnumDescriptor(
  name='MLSetupStatus',
  full_name='contract_learn.grpc.MLSetupStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1096,
  serialized_end=1150,
)
_sym_db.RegisterEnumDescriptor(_MLSETUPSTATUS)

MLSetupStatus = enum_type_wrapper.EnumTypeWrapper(_MLSETUPSTATUS)
_SYSTEMSTATUS = _descriptor.EnumDescriptor(
  name='SystemStatus',
  full_name='contract_learn.grpc.SystemStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WORKING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO_MODEL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1152,
  serialized_end=1226,
)
_sym_db.RegisterEnumDescriptor(_SYSTEMSTATUS)

SystemStatus = enum_type_wrapper.EnumTypeWrapper(_SYSTEMSTATUS)
UNDEFINED = 0
SUCCESS = 1
ERROR = 2
WORKING = 0
NO_MODEL = 1
INTERNAL_ERROR = 2
UNKNOWN = 3



_REQUESTMLSETUP = _descriptor.Descriptor(
  name='RequestMLSetup',
  full_name='contract_learn.grpc.RequestMLSetup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_loader_name', full_name='contract_learn.grpc.RequestMLSetup.dataset_loader_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataset_loader_parameters', full_name='contract_learn.grpc.RequestMLSetup.dataset_loader_parameters', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_arch_name', full_name='contract_learn.grpc.RequestMLSetup.model_arch_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_parameters', full_name='contract_learn.grpc.RequestMLSetup.model_parameters', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=70,
  serialized_end=201,
)


_RESPONSEMLSETUP = _descriptor.Descriptor(
  name='ResponseMLSetup',
  full_name='contract_learn.grpc.ResponseMLSetup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='contract_learn.grpc.ResponseMLSetup.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='contract_learn.grpc.ResponseMLSetup.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=203,
  serialized_end=293,
)


_WEIGHTS = _descriptor.Descriptor(
  name='Weights',
  full_name='contract_learn.grpc.Weights',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='weights', full_name='contract_learn.grpc.Weights.weights', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=295,
  serialized_end=321,
)


_PROPOSEDWEIGHTS_EVALUATIONRESULTSENTRY = _descriptor.Descriptor(
  name='EvaluationResultsEntry',
  full_name='contract_learn.grpc.ProposedWeights.EvaluationResultsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='contract_learn.grpc.ProposedWeights.EvaluationResultsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='contract_learn.grpc.ProposedWeights.EvaluationResultsEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=533,
  serialized_end=589,
)

_PROPOSEDWEIGHTS = _descriptor.Descriptor(
  name='ProposedWeights',
  full_name='contract_learn.grpc.ProposedWeights',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='weights', full_name='contract_learn.grpc.ProposedWeights.weights', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vote_score', full_name='contract_learn.grpc.ProposedWeights.vote_score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='test_score', full_name='contract_learn.grpc.ProposedWeights.test_score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vote', full_name='contract_learn.grpc.ProposedWeights.vote', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='evaluation_results', full_name='contract_learn.grpc.ProposedWeights.evaluation_results', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PROPOSEDWEIGHTS_EVALUATIONRESULTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=589,
)


_REQUESTSTATUS = _descriptor.Descriptor(
  name='RequestStatus',
  full_name='contract_learn.grpc.RequestStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=591,
  serialized_end=606,
)


_RESPONSESTATUS = _descriptor.Descriptor(
  name='ResponseStatus',
  full_name='contract_learn.grpc.ResponseStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='contract_learn.grpc.ResponseStatus.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=608,
  serialized_end=675,
)


_DATASETLOADERSPEC = _descriptor.Descriptor(
  name='DatasetLoaderSpec',
  full_name='contract_learn.grpc.DatasetLoaderSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='contract_learn.grpc.DatasetLoaderSpec.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_parameters', full_name='contract_learn.grpc.DatasetLoaderSpec.default_parameters', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=677,
  serialized_end=738,
)


_MODELARCHSPEC = _descriptor.Descriptor(
  name='ModelArchSpec',
  full_name='contract_learn.grpc.ModelArchSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='contract_learn.grpc.ModelArchSpec.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_parameters', full_name='contract_learn.grpc.ModelArchSpec.default_parameters', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=740,
  serialized_end=797,
)


_RESPONSESUPPORTEDSYSTEM_COMPATIBILITYENTRY = _descriptor.Descriptor(
  name='CompatibilityEntry',
  full_name='contract_learn.grpc.ResponseSupportedSystem.CompatibilityEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='contract_learn.grpc.ResponseSupportedSystem.CompatibilityEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='contract_learn.grpc.ResponseSupportedSystem.CompatibilityEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1042,
  serialized_end=1094,
)

_RESPONSESUPPORTEDSYSTEM = _descriptor.Descriptor(
  name='ResponseSupportedSystem',
  full_name='contract_learn.grpc.ResponseSupportedSystem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_loaders', full_name='contract_learn.grpc.ResponseSupportedSystem.data_loaders', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_architectures', full_name='contract_learn.grpc.ResponseSupportedSystem.model_architectures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compatibility', full_name='contract_learn.grpc.ResponseSupportedSystem.compatibility', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSESUPPORTEDSYSTEM_COMPATIBILITYENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=800,
  serialized_end=1094,
)

_RESPONSEMLSETUP.fields_by_name['status'].enum_type = _MLSETUPSTATUS
_PROPOSEDWEIGHTS_EVALUATIONRESULTSENTRY.containing_type = _PROPOSEDWEIGHTS
_PROPOSEDWEIGHTS.fields_by_name['weights'].message_type = _WEIGHTS
_PROPOSEDWEIGHTS.fields_by_name['evaluation_results'].message_type = _PROPOSEDWEIGHTS_EVALUATIONRESULTSENTRY
_RESPONSESTATUS.fields_by_name['status'].enum_type = _SYSTEMSTATUS
_RESPONSESUPPORTEDSYSTEM_COMPATIBILITYENTRY.containing_type = _RESPONSESUPPORTEDSYSTEM
_RESPONSESUPPORTEDSYSTEM.fields_by_name['data_loaders'].message_type = _DATASETLOADERSPEC
_RESPONSESUPPORTEDSYSTEM.fields_by_name['model_architectures'].message_type = _MODELARCHSPEC
_RESPONSESUPPORTEDSYSTEM.fields_by_name['compatibility'].message_type = _RESPONSESUPPORTEDSYSTEM_COMPATIBILITYENTRY
DESCRIPTOR.message_types_by_name['RequestMLSetup'] = _REQUESTMLSETUP
DESCRIPTOR.message_types_by_name['ResponseMLSetup'] = _RESPONSEMLSETUP
DESCRIPTOR.message_types_by_name['Weights'] = _WEIGHTS
DESCRIPTOR.message_types_by_name['ProposedWeights'] = _PROPOSEDWEIGHTS
DESCRIPTOR.message_types_by_name['RequestStatus'] = _REQUESTSTATUS
DESCRIPTOR.message_types_by_name['ResponseStatus'] = _RESPONSESTATUS
DESCRIPTOR.message_types_by_name['DatasetLoaderSpec'] = _DATASETLOADERSPEC
DESCRIPTOR.message_types_by_name['ModelArchSpec'] = _MODELARCHSPEC
DESCRIPTOR.message_types_by_name['ResponseSupportedSystem'] = _RESPONSESUPPORTEDSYSTEM
DESCRIPTOR.enum_types_by_name['MLSetupStatus'] = _MLSETUPSTATUS
DESCRIPTOR.enum_types_by_name['SystemStatus'] = _SYSTEMSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestMLSetup = _reflection.GeneratedProtocolMessageType('RequestMLSetup', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTMLSETUP,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:contract_learn.grpc.RequestMLSetup)
  })
_sym_db.RegisterMessage(RequestMLSetup)

ResponseMLSetup = _reflection.GeneratedProtocolMessageType('ResponseMLSetup', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEMLSETUP,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:contract_learn.grpc.ResponseMLSetup)
  })
_sym_db.RegisterMessage(ResponseMLSetup)

Weights = _reflection.GeneratedProtocolMessageType('Weights', (_message.Message,), {
  'DESCRIPTOR' : _WEIGHTS,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:contract_learn.grpc.Weights)
  })
_sym_db.RegisterMessage(Weights)

ProposedWeights = _reflection.GeneratedProtocolMessageType('ProposedWeights', (_message.Message,), {

  'EvaluationResultsEntry' : _reflection.GeneratedProtocolMessageType('EvaluationResultsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PROPOSEDWEIGHTS_EVALUATIONRESULTSENTRY,
    '__module__' : 'interface_pb2'
    # @@protoc_insertion_point(class_scope:contract_learn.grpc.ProposedWeights.EvaluationResultsEntry)
    })
  ,
  'DESCRIPTOR' : _PROPOSEDWEIGHTS,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:contract_learn.grpc.ProposedWeights)
  })
_sym_db.RegisterMessage(ProposedWeights)
_sym_db.RegisterMessage(ProposedWeights.EvaluationResultsEntry)

RequestStatus = _reflection.GeneratedProtocolMessageType('RequestStatus', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTSTATUS,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:contract_learn.grpc.RequestStatus)
  })
_sym_db.RegisterMessage(RequestStatus)

ResponseStatus = _reflection.GeneratedProtocolMessageType('ResponseStatus', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSESTATUS,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:contract_learn.grpc.ResponseStatus)
  })
_sym_db.RegisterMessage(ResponseStatus)

DatasetLoaderSpec = _reflection.GeneratedProtocolMessageType('DatasetLoaderSpec', (_message.Message,), {
  'DESCRIPTOR' : _DATASETLOADERSPEC,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:contract_learn.grpc.DatasetLoaderSpec)
  })
_sym_db.RegisterMessage(DatasetLoaderSpec)

ModelArchSpec = _reflection.GeneratedProtocolMessageType('ModelArchSpec', (_message.Message,), {
  'DESCRIPTOR' : _MODELARCHSPEC,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:contract_learn.grpc.ModelArchSpec)
  })
_sym_db.RegisterMessage(ModelArchSpec)

ResponseSupportedSystem = _reflection.GeneratedProtocolMessageType('ResponseSupportedSystem', (_message.Message,), {

  'CompatibilityEntry' : _reflection.GeneratedProtocolMessageType('CompatibilityEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSESUPPORTEDSYSTEM_COMPATIBILITYENTRY,
    '__module__' : 'interface_pb2'
    # @@protoc_insertion_point(class_scope:contract_learn.grpc.ResponseSupportedSystem.CompatibilityEntry)
    })
  ,
  'DESCRIPTOR' : _RESPONSESUPPORTEDSYSTEM,
  '__module__' : 'interface_pb2'
  # @@protoc_insertion_point(class_scope:contract_learn.grpc.ResponseSupportedSystem)
  })
_sym_db.RegisterMessage(ResponseSupportedSystem)
_sym_db.RegisterMessage(ResponseSupportedSystem.CompatibilityEntry)


_PROPOSEDWEIGHTS_EVALUATIONRESULTSENTRY._options = None
_RESPONSESUPPORTEDSYSTEM_COMPATIBILITYENTRY._options = None

_GRPCLEARNER = _descriptor.ServiceDescriptor(
  name='GRPCLearner',
  full_name='contract_learn.grpc.GRPCLearner',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1229,
  serialized_end=1740,
  methods=[
  _descriptor.MethodDescriptor(
    name='QuerySupportedSystem',
    full_name='contract_learn.grpc.GRPCLearner.QuerySupportedSystem',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_RESPONSESUPPORTEDSYSTEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MLSetup',
    full_name='contract_learn.grpc.GRPCLearner.MLSetup',
    index=1,
    containing_service=None,
    input_type=_REQUESTMLSETUP,
    output_type=_RESPONSEMLSETUP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ProposeWeights',
    full_name='contract_learn.grpc.GRPCLearner.ProposeWeights',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_WEIGHTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestWeights',
    full_name='contract_learn.grpc.GRPCLearner.TestWeights',
    index=3,
    containing_service=None,
    input_type=_WEIGHTS,
    output_type=_PROPOSEDWEIGHTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetWeights',
    full_name='contract_learn.grpc.GRPCLearner.SetWeights',
    index=4,
    containing_service=None,
    input_type=_WEIGHTS,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StatusStream',
    full_name='contract_learn.grpc.GRPCLearner.StatusStream',
    index=5,
    containing_service=None,
    input_type=_REQUESTSTATUS,
    output_type=_RESPONSESTATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRPCLEARNER)

DESCRIPTOR.services_by_name['GRPCLearner'] = _GRPCLEARNER

# @@protoc_insertion_point(module_scope)