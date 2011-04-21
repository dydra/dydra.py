__version__ = '0.0.0'

HOST     = 'api.dydra.com'
BASE_URL = 'http://' + HOST + '/'
AUTH_URL = 'http://%s:%s@' + HOST + '/'

from dydra.client import Client
