import dydra

class Repository(dydra.Resource):
  """An RDF repository on Dydra.com."""

  name = None

  def __init__(self, name, **kwargs):
    self.name = str(name)
    super(Repository, self).__init__(self.name, **kwargs)

  def __repr__(self):
    return "dydra.Repository('%s')" % (self.name)

  def __len__(self):
    return self.count()

  def count(self):
    return self.client.call('repository.count', self.name)

  def clear(self):
    return self.client.call('repository.clear', self.name)
