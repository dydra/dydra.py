import dydra

class Query(dydra.Resource):
  """A SPARQL query on Dydra.com."""

  name = None

  def __init__(self, name, **kwargs):
    self.name = str(name)
    super(Query, self).__init__(self.name, **kwargs)

  def __repr__(self):
    return "dydra.Query('%s')" % (self.name)
