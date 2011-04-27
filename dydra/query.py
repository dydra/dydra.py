import dydra

##
# Represents a Dydra.com SPARQL query.
#
# @see http://docs.dydra.com/sdk/python
class Query(dydra.Resource):
  """Represents a Dydra.com SPARQL query."""

  ##
  # (Attribute) The query name.
  name = None

  ##
  # @param name A valid query name.
  def __init__(self, name, **kwargs):
    self.name = str(name)
    super(Query, self).__init__(self.name, **kwargs)

  ##
  # @return A string representation of this object.
  def __repr__(self):
    return "dydra.Query('%s')" % (self.name)
