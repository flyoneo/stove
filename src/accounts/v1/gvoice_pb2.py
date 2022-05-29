# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: accounts/v1/gvoice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61\x63\x63ounts/v1/gvoice.proto\"^\n\x0eSendSMSRequest\x12\x1b\n\x13gvoice_phone_number\x18\x01 \x02(\t\x12\x1e\n\x16recipient_phone_number\x18\x02 \x02(\t\x12\x0f\n\x07message\x18\x03 \x02(\t\"3\n\x0fSendSMSResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x05\x65rror\x18\x02 \x01(\t:\x00\"6\n\x17\x46\x65tchContactListRequest\x12\x1b\n\x13gvoice_phone_number\x18\x01 \x02(\t\"]\n\x18\x46\x65tchContactListResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x05\x65rror\x18\x02 \x01(\t:\x00\x12\x1f\n\x17recipient_phone_numbers\x18\x03 \x03(\t\"\x1b\n\x19\x46\x65tchGVoiceNumbersRequest\"\\\n\x1a\x46\x65tchGVoiceNumbersResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x05\x65rror\x18\x02 \x01(\t:\x00\x12\x1c\n\x14gvoice_phone_numbers\x18\x03 \x03(\t\"r\n\x1a\x46\x65tchContactHistoryRequest\x12\x1b\n\x13gvoice_phone_number\x18\x01 \x02(\t\x12\x1e\n\x16recipient_phone_number\x18\x02 \x02(\t\x12\x17\n\x0cnum_messages\x18\x03 \x02(\x04:\x01\x30\"_\n\x1b\x46\x65tchContactHistoryResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x05\x65rror\x18\x02 \x01(\t:\x00\x12\x1e\n\x08messages\x18\x03 \x03(\x0b\x32\x0c.MessageNode\"J\n\x0bMessageNode\x12\x11\n\ttimestamp\x18\x01 \x02(\x04\x12\x18\n\x10message_contents\x18\x02 \x02(\t\x12\x0e\n\x06source\x18\x03 \x02(\x08\x32\xa2\x02\n\x06GVoice\x12.\n\x07SendSMS\x12\x0f.SendSMSRequest\x1a\x10.SendSMSResponse\"\x00\x12G\n\x0eGetContactList\x12\x18.FetchContactListRequest\x1a\x19.FetchContactListResponse\"\x00\x12M\n\x10GetGVoiceNumbers\x12\x1a.FetchGVoiceNumbersRequest\x1a\x1b.FetchGVoiceNumbersResponse\"\x00\x12P\n\x11GetContactHistory\x12\x1b.FetchContactHistoryRequest\x1a\x1c.FetchContactHistoryResponse\"\x00\x42.Z,github.com/kingcobra2468/cot/internal/gvoice')



_SENDSMSREQUEST = DESCRIPTOR.message_types_by_name['SendSMSRequest']
_SENDSMSRESPONSE = DESCRIPTOR.message_types_by_name['SendSMSResponse']
_FETCHCONTACTLISTREQUEST = DESCRIPTOR.message_types_by_name['FetchContactListRequest']
_FETCHCONTACTLISTRESPONSE = DESCRIPTOR.message_types_by_name['FetchContactListResponse']
_FETCHGVOICENUMBERSREQUEST = DESCRIPTOR.message_types_by_name['FetchGVoiceNumbersRequest']
_FETCHGVOICENUMBERSRESPONSE = DESCRIPTOR.message_types_by_name['FetchGVoiceNumbersResponse']
_FETCHCONTACTHISTORYREQUEST = DESCRIPTOR.message_types_by_name['FetchContactHistoryRequest']
_FETCHCONTACTHISTORYRESPONSE = DESCRIPTOR.message_types_by_name['FetchContactHistoryResponse']
_MESSAGENODE = DESCRIPTOR.message_types_by_name['MessageNode']
SendSMSRequest = _reflection.GeneratedProtocolMessageType('SendSMSRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDSMSREQUEST,
  '__module__' : 'accounts.v1.gvoice_pb2'
  # @@protoc_insertion_point(class_scope:SendSMSRequest)
  })
_sym_db.RegisterMessage(SendSMSRequest)

SendSMSResponse = _reflection.GeneratedProtocolMessageType('SendSMSResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDSMSRESPONSE,
  '__module__' : 'accounts.v1.gvoice_pb2'
  # @@protoc_insertion_point(class_scope:SendSMSResponse)
  })
_sym_db.RegisterMessage(SendSMSResponse)

FetchContactListRequest = _reflection.GeneratedProtocolMessageType('FetchContactListRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHCONTACTLISTREQUEST,
  '__module__' : 'accounts.v1.gvoice_pb2'
  # @@protoc_insertion_point(class_scope:FetchContactListRequest)
  })
_sym_db.RegisterMessage(FetchContactListRequest)

FetchContactListResponse = _reflection.GeneratedProtocolMessageType('FetchContactListResponse', (_message.Message,), {
  'DESCRIPTOR' : _FETCHCONTACTLISTRESPONSE,
  '__module__' : 'accounts.v1.gvoice_pb2'
  # @@protoc_insertion_point(class_scope:FetchContactListResponse)
  })
_sym_db.RegisterMessage(FetchContactListResponse)

FetchGVoiceNumbersRequest = _reflection.GeneratedProtocolMessageType('FetchGVoiceNumbersRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHGVOICENUMBERSREQUEST,
  '__module__' : 'accounts.v1.gvoice_pb2'
  # @@protoc_insertion_point(class_scope:FetchGVoiceNumbersRequest)
  })
_sym_db.RegisterMessage(FetchGVoiceNumbersRequest)

FetchGVoiceNumbersResponse = _reflection.GeneratedProtocolMessageType('FetchGVoiceNumbersResponse', (_message.Message,), {
  'DESCRIPTOR' : _FETCHGVOICENUMBERSRESPONSE,
  '__module__' : 'accounts.v1.gvoice_pb2'
  # @@protoc_insertion_point(class_scope:FetchGVoiceNumbersResponse)
  })
_sym_db.RegisterMessage(FetchGVoiceNumbersResponse)

FetchContactHistoryRequest = _reflection.GeneratedProtocolMessageType('FetchContactHistoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHCONTACTHISTORYREQUEST,
  '__module__' : 'accounts.v1.gvoice_pb2'
  # @@protoc_insertion_point(class_scope:FetchContactHistoryRequest)
  })
_sym_db.RegisterMessage(FetchContactHistoryRequest)

FetchContactHistoryResponse = _reflection.GeneratedProtocolMessageType('FetchContactHistoryResponse', (_message.Message,), {
  'DESCRIPTOR' : _FETCHCONTACTHISTORYRESPONSE,
  '__module__' : 'accounts.v1.gvoice_pb2'
  # @@protoc_insertion_point(class_scope:FetchContactHistoryResponse)
  })
_sym_db.RegisterMessage(FetchContactHistoryResponse)

MessageNode = _reflection.GeneratedProtocolMessageType('MessageNode', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGENODE,
  '__module__' : 'accounts.v1.gvoice_pb2'
  # @@protoc_insertion_point(class_scope:MessageNode)
  })
_sym_db.RegisterMessage(MessageNode)

_GVOICE = DESCRIPTOR.services_by_name['GVoice']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/kingcobra2468/cot/internal/gvoice'
  _SENDSMSREQUEST._serialized_start=28
  _SENDSMSREQUEST._serialized_end=122
  _SENDSMSRESPONSE._serialized_start=124
  _SENDSMSRESPONSE._serialized_end=175
  _FETCHCONTACTLISTREQUEST._serialized_start=177
  _FETCHCONTACTLISTREQUEST._serialized_end=231
  _FETCHCONTACTLISTRESPONSE._serialized_start=233
  _FETCHCONTACTLISTRESPONSE._serialized_end=326
  _FETCHGVOICENUMBERSREQUEST._serialized_start=328
  _FETCHGVOICENUMBERSREQUEST._serialized_end=355
  _FETCHGVOICENUMBERSRESPONSE._serialized_start=357
  _FETCHGVOICENUMBERSRESPONSE._serialized_end=449
  _FETCHCONTACTHISTORYREQUEST._serialized_start=451
  _FETCHCONTACTHISTORYREQUEST._serialized_end=565
  _FETCHCONTACTHISTORYRESPONSE._serialized_start=567
  _FETCHCONTACTHISTORYRESPONSE._serialized_end=662
  _MESSAGENODE._serialized_start=664
  _MESSAGENODE._serialized_end=738
  _GVOICE._serialized_start=741
  _GVOICE._serialized_end=1031
# @@protoc_insertion_point(module_scope)