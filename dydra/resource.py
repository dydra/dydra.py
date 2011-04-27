import dydra
import urllib2 # FIXME: urllib.request in Python 3.0+

##
# Represents a Dydra.com resource.
#
# This is the base class for all classes that represent dereferenceable HTTP
# resources on Dydra.com.
#
# @see http://docs.dydra.com/sdk/python
# @see http://docs.dydra.com/api/rest
class Resource(object):
  """Represents a Dydra.com resource."""

  path   = None
  url    = None
  client = None

  ##
  # @param path A root-relative resource path, without the initial slash.
  def __init__(self, path, **kwargs):
    self.path   = str(path)
    self.url    = dydra.BASE_URL + self.path
    if kwargs.has_key('client'):
      self.client = kwargs['client']

  ##
  # @return A string representation of this object.
  def __repr__(self):
    return "dydra.Resource('%s')" % (self.path)

  ##
  # Checks whether this resource exists.
  #
  # @return A boolean.
  def exists(self):
    try:
      response = urllib2.urlopen(self.request(method='HEAD'))
      return True
    except urllib2.HTTPError, error:
      if error.code == 404:
        return False
      return None

  def request(self, **kwargs):
    request = urllib2.Request(self.auth_url())
    if kwargs.has_key('method'):
      request.get_method = lambda: kwargs['method']
    return request

  def auth_url(self):
    url = self.url
    if self.client and self.client.token:
      url += '?auth_token=' + self.client.token
    return url
