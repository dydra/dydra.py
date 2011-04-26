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

  def create(self):
    return self.client.call('repository.create', self.name)

  def destroy(self):
    return self.client.call('repository.destroy', self.name)

  def count(self):
    return self.client.call('repository.count', self.name)

  def clear(self):
    return dydra.Job(self.client.call('repository.clear', self.name), client=self.client)

  def import_from_url(self, url, **kwargs):
    url, context, base_uri = str(url), '', ''
    if kwargs.has_key('context') and kwargs['context']:
      context = str(kwargs['context'])
    if kwargs.has_key('base_uri') and kwargs['base_uri']:
      base_uri = str(kwargs['base_uri'])
    return dydra.Job(self.client.call('repository.import', self.name, url, context, base_uri), client=self.client)
