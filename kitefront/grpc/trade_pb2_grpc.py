# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import trade_pb2 as trade__pb2


class TradeStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Orders = channel.unary_unary(
        '/fisk.broker.Trade/Orders',
        request_serializer=trade__pb2.OrdersRequest.SerializeToString,
        response_deserializer=trade__pb2.OrdersResponse.FromString,
        )
    self.PlaceOrder = channel.unary_unary(
        '/fisk.broker.Trade/PlaceOrder',
        request_serializer=trade__pb2.PlaceOrderRequest.SerializeToString,
        response_deserializer=trade__pb2.PlaceOrderResponse.FromString,
        )
    self.UpdateOrder = channel.unary_unary(
        '/fisk.broker.Trade/UpdateOrder',
        request_serializer=trade__pb2.UpdateOrderRequest.SerializeToString,
        response_deserializer=trade__pb2.UpdateOrderResponse.FromString,
        )
    self.CancelOrder = channel.unary_unary(
        '/fisk.broker.Trade/CancelOrder',
        request_serializer=trade__pb2.CancelOrderRequest.SerializeToString,
        response_deserializer=trade__pb2.CancelOrderResponse.FromString,
        )
    self.Holdings = channel.unary_unary(
        '/fisk.broker.Trade/Holdings',
        request_serializer=trade__pb2.HoldingsRequest.SerializeToString,
        response_deserializer=trade__pb2.HoldingsResponse.FromString,
        )
    self.Positions = channel.unary_unary(
        '/fisk.broker.Trade/Positions',
        request_serializer=trade__pb2.PositionsRequest.SerializeToString,
        response_deserializer=trade__pb2.PositionsResponse.FromString,
        )


class TradeServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Orders(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PlaceOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CancelOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Holdings(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Positions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TradeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Orders': grpc.unary_unary_rpc_method_handler(
          servicer.Orders,
          request_deserializer=trade__pb2.OrdersRequest.FromString,
          response_serializer=trade__pb2.OrdersResponse.SerializeToString,
      ),
      'PlaceOrder': grpc.unary_unary_rpc_method_handler(
          servicer.PlaceOrder,
          request_deserializer=trade__pb2.PlaceOrderRequest.FromString,
          response_serializer=trade__pb2.PlaceOrderResponse.SerializeToString,
      ),
      'UpdateOrder': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateOrder,
          request_deserializer=trade__pb2.UpdateOrderRequest.FromString,
          response_serializer=trade__pb2.UpdateOrderResponse.SerializeToString,
      ),
      'CancelOrder': grpc.unary_unary_rpc_method_handler(
          servicer.CancelOrder,
          request_deserializer=trade__pb2.CancelOrderRequest.FromString,
          response_serializer=trade__pb2.CancelOrderResponse.SerializeToString,
      ),
      'Holdings': grpc.unary_unary_rpc_method_handler(
          servicer.Holdings,
          request_deserializer=trade__pb2.HoldingsRequest.FromString,
          response_serializer=trade__pb2.HoldingsResponse.SerializeToString,
      ),
      'Positions': grpc.unary_unary_rpc_method_handler(
          servicer.Positions,
          request_deserializer=trade__pb2.PositionsRequest.FromString,
          response_serializer=trade__pb2.PositionsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fisk.broker.Trade', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))