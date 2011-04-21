import dydra

class Resource(object):
  """A resource on Dydra.com."""

  path   = None
  url    = None
  client = None

  def __init__(self, path, **kwargs):
    self.path   = str(path)
    self.url    = dydra.BASE_URL + self.path
    if kwargs.has_key('client'):
      self.client = kwargs['client']

  def __repr__(self):
    return "dydra.Resource('%s')" % (self.path)

  def exists(self):
    return True # FIXME
