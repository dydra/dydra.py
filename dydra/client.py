import dydra
import xmlrpclib # FIXME: xmlrpc.client in Python 3.0+

##
# Implements a Dydra.com XML-RPC API client.
#
# @see http://docs.dydra.com/sdk/python
# @see http://docs.dydra.com/api/rpc
class Client(object):
  """Implements a Dydra.com XML-RPC API client."""

  url      = None
  token    = None
  username = None
  password = None
  rpc      = None

  def __init__(self, **kwargs):
    if kwargs.has_key('url'):
      self.url = str(kwargs['url'])
    elif kwargs.has_key('token'):
      self.token = str(kwargs['token'])
      self.url = dydra.BASE_URL + 'rpc?auth_token=' + self.token
    elif kwargs.has_key('username') and kwargs.has_key('password'):
      self.username = str(kwargs['username'])
      self.password = str(kwargs['password'])
      self.url = (dydra.AUTH_URL % (self.username, self.password)) + 'rpc'
    else:
      raise RuntimeError('no user credentials supplied')
    self.rpc = xmlrpclib.ServerProxy(self.url)

  ##
  # @return A string representation of this object.
  def __repr__(self):
    return "dydra.Client(url='%s')" % (self.url)

  ##
  # @param method The RPC method to call.
  # @return The RPC method's result.
  def __call__(self, method, *args):
    return getattr(self.rpc, 'dydra.' + method)(*args)

  ##
  # Invokes a given RPC method.
  #
  # @param method The RPC method to call.
  # @return The RPC method's result.
  def call(self, method, *args):
    return self.__call__(method, *args)
