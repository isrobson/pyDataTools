# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import featureselector_pb2 as featureselector__pb2


class FeatureSelectorStub(object):
  """define a feature selection service
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.fsLassoCV = channel.unary_unary(
        '/featureselector.FeatureSelector/fsLassoCV',
        request_serializer=featureselector__pb2.numericArray.SerializeToString,
        response_deserializer=featureselector__pb2.stringList.FromString,
        )


class FeatureSelectorServicer(object):
  """define a feature selection service
  """

  def fsLassoCV(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FeatureSelectorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'fsLassoCV': grpc.unary_unary_rpc_method_handler(
          servicer.fsLassoCV,
          request_deserializer=featureselector__pb2.numericArray.FromString,
          response_serializer=featureselector__pb2.stringList.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'featureselector.FeatureSelector', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))