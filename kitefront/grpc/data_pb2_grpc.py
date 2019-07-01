# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import data_pb2 as data__pb2


class DataStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Candles = channel.unary_unary(
        '/fisk.broker.Data/Candles',
        request_serializer=data__pb2.CandlesRequest.SerializeToString,
        response_deserializer=data__pb2.CandlesResponse.FromString,
        )


class DataServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Candles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DataServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Candles': grpc.unary_unary_rpc_method_handler(
          servicer.Candles,
          request_deserializer=data__pb2.CandlesRequest.FromString,
          response_serializer=data__pb2.CandlesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fisk.broker.Data', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))