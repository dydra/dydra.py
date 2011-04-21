import dydra
import xmlrpclib # FIXME: xmlrpc.client in Python 3.0+

class Client(object):
  """A client for the Dydra.com XML-RPC API."""

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

  def __repr__(self):
    return "dydra.Client(url='%s')" % (self.url)

  def __call__(self, method, *args):
    return getattr(self.rpc, 'dydra.' + method)(*args)

  def call(self, method, *args):
    return self.__call__(method, *args)
