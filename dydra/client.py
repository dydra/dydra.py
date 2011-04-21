import dydra
import xmlrpclib # FIXME: use xmlrpc.client for Python 3.0+

class Client(object):
  """A client for the Dydra.com XML-RPC API."""

  url = None
  rpc = None

  def __init__(self, **kwargs):
    if kwargs.has_key('url'):
      self.url = str(kwargs['url'])
    elif kwargs.has_key('token'):
      self.url = dydra.BASE_URL + 'rpc?auth_token=' + str(kwargs['token'])
    elif kwargs.has_key('username') and kwargs.has_key('password'):
      self.url = (dydra.AUTH_URL % (str(kwargs['username']), str(kwargs['password']))) + 'rpc'
    else:
      raise RuntimeError('no user credentials supplied')
    self.rpc = xmlrpclib.ServerProxy(self.url)

  def __repr__(self):
    return "dydra.Client(url='%s')" % (self.url)

  def __call__(self, method, *args):
    return getattr(self.rpc, 'dydra.' + method)(*args)

  def call(self, method, *args):
    return self.__call__(method, *args)
