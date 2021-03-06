# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sms.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sms.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\tsms.proto\"_\n\x0eSendSMSRequest\x12\x0e\n\x06mobile\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61ptcha\x18\x02 \x01(\t\x12\x17\n\x0f\x65xpired_minutes\x18\x03 \x01(\x05\x12\x13\n\x0btemplate_id\x18\x04 \x01(\x05\"\x1e\n\x0fSendSMSResponse\x12\x0b\n\x03ret\x18\x01 \x01(\x05\"G\n\x10SendVoiceRequest\x12\x0e\n\x06mobile\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61ptcha\x18\x02 \x01(\t\x12\x12\n\nplay_times\x18\x03 \x01(\x05\" \n\x11SendVoiceResponse\x12\x0b\n\x03ret\x18\x01 \x01(\x05\x32\x84\x01\n\x0e\x43\x61ptchaService\x12\x35\n\x0eSendSMSCaptcha\x12\x0f.SendSMSRequest\x1a\x10.SendSMSResponse\"\x00\x12;\n\x10SendVoiceCaptcha\x12\x11.SendVoiceRequest\x1a\x12.SendVoiceResponse\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SENDSMSREQUEST = _descriptor.Descriptor(
  name='SendSMSRequest',
  full_name='SendSMSRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mobile', full_name='SendSMSRequest.mobile', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='captcha', full_name='SendSMSRequest.captcha', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expired_minutes', full_name='SendSMSRequest.expired_minutes', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='SendSMSRequest.template_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=108,
)


_SENDSMSRESPONSE = _descriptor.Descriptor(
  name='SendSMSResponse',
  full_name='SendSMSResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='SendSMSResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=140,
)


_SENDVOICEREQUEST = _descriptor.Descriptor(
  name='SendVoiceRequest',
  full_name='SendVoiceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mobile', full_name='SendVoiceRequest.mobile', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='captcha', full_name='SendVoiceRequest.captcha', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='play_times', full_name='SendVoiceRequest.play_times', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=213,
)


_SENDVOICERESPONSE = _descriptor.Descriptor(
  name='SendVoiceResponse',
  full_name='SendVoiceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='SendVoiceResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=247,
)

DESCRIPTOR.message_types_by_name['SendSMSRequest'] = _SENDSMSREQUEST
DESCRIPTOR.message_types_by_name['SendSMSResponse'] = _SENDSMSRESPONSE
DESCRIPTOR.message_types_by_name['SendVoiceRequest'] = _SENDVOICEREQUEST
DESCRIPTOR.message_types_by_name['SendVoiceResponse'] = _SENDVOICERESPONSE

SendSMSRequest = _reflection.GeneratedProtocolMessageType('SendSMSRequest', (_message.Message,), dict(
  DESCRIPTOR = _SENDSMSREQUEST,
  __module__ = 'sms_pb2'
  # @@protoc_insertion_point(class_scope:SendSMSRequest)
  ))
_sym_db.RegisterMessage(SendSMSRequest)

SendSMSResponse = _reflection.GeneratedProtocolMessageType('SendSMSResponse', (_message.Message,), dict(
  DESCRIPTOR = _SENDSMSRESPONSE,
  __module__ = 'sms_pb2'
  # @@protoc_insertion_point(class_scope:SendSMSResponse)
  ))
_sym_db.RegisterMessage(SendSMSResponse)

SendVoiceRequest = _reflection.GeneratedProtocolMessageType('SendVoiceRequest', (_message.Message,), dict(
  DESCRIPTOR = _SENDVOICEREQUEST,
  __module__ = 'sms_pb2'
  # @@protoc_insertion_point(class_scope:SendVoiceRequest)
  ))
_sym_db.RegisterMessage(SendVoiceRequest)

SendVoiceResponse = _reflection.GeneratedProtocolMessageType('SendVoiceResponse', (_message.Message,), dict(
  DESCRIPTOR = _SENDVOICERESPONSE,
  __module__ = 'sms_pb2'
  # @@protoc_insertion_point(class_scope:SendVoiceResponse)
  ))
_sym_db.RegisterMessage(SendVoiceResponse)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class CaptchaServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendSMSCaptcha = channel.unary_unary(
        '/CaptchaService/SendSMSCaptcha',
        request_serializer=SendSMSRequest.SerializeToString,
        response_deserializer=SendSMSResponse.FromString,
        )
    self.SendVoiceCaptcha = channel.unary_unary(
        '/CaptchaService/SendVoiceCaptcha',
        request_serializer=SendVoiceRequest.SerializeToString,
        response_deserializer=SendVoiceResponse.FromString,
        )


class CaptchaServiceServicer(object):

  def SendSMSCaptcha(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendVoiceCaptcha(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CaptchaServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendSMSCaptcha': grpc.unary_unary_rpc_method_handler(
          servicer.SendSMSCaptcha,
          request_deserializer=SendSMSRequest.FromString,
          response_serializer=SendSMSResponse.SerializeToString,
      ),
      'SendVoiceCaptcha': grpc.unary_unary_rpc_method_handler(
          servicer.SendVoiceCaptcha,
          request_deserializer=SendVoiceRequest.FromString,
          response_serializer=SendVoiceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'CaptchaService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaCaptchaServiceServicer(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def SendSMSCaptcha(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def SendVoiceCaptcha(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaCaptchaServiceStub(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def SendSMSCaptcha(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  SendSMSCaptcha.future = None
  def SendVoiceCaptcha(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  SendVoiceCaptcha.future = None


def beta_create_CaptchaService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_deserializers = {
    ('CaptchaService', 'SendSMSCaptcha'): SendSMSRequest.FromString,
    ('CaptchaService', 'SendVoiceCaptcha'): SendVoiceRequest.FromString,
  }
  response_serializers = {
    ('CaptchaService', 'SendSMSCaptcha'): SendSMSResponse.SerializeToString,
    ('CaptchaService', 'SendVoiceCaptcha'): SendVoiceResponse.SerializeToString,
  }
  method_implementations = {
    ('CaptchaService', 'SendSMSCaptcha'): face_utilities.unary_unary_inline(servicer.SendSMSCaptcha),
    ('CaptchaService', 'SendVoiceCaptcha'): face_utilities.unary_unary_inline(servicer.SendVoiceCaptcha),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_CaptchaService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_serializers = {
    ('CaptchaService', 'SendSMSCaptcha'): SendSMSRequest.SerializeToString,
    ('CaptchaService', 'SendVoiceCaptcha'): SendVoiceRequest.SerializeToString,
  }
  response_deserializers = {
    ('CaptchaService', 'SendSMSCaptcha'): SendSMSResponse.FromString,
    ('CaptchaService', 'SendVoiceCaptcha'): SendVoiceResponse.FromString,
  }
  cardinalities = {
    'SendSMSCaptcha': cardinality.Cardinality.UNARY_UNARY,
    'SendVoiceCaptcha': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'CaptchaService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
