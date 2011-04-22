__version__ = '0.0.2'

HOST     = 'api.dydra.com'
BASE_URL = 'http://' + HOST + '/'
AUTH_URL = 'http://%s:%s@' + HOST + '/'

from dydra.client     import Client
from dydra.resource   import Resource
from dydra.account    import Account
from dydra.repository import Repository
from dydra.query      import Query
from dydra.job        import Job
