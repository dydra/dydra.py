import dydra

class Account(dydra.Resource):
  """A user account on Dydra.com."""

  name = None

  def __init__(self, name, **kwargs):
    self.name = str(name)
    super(Account, self).__init__(self.name, **kwargs)

  def __repr__(self):
    return "dydra.Account('%s')" % (self.name)

  def __getitem__(self, key):
    return dydra.Repository(self.name + '/' + str(key), client=self.client)

  def __iter__(self):
    repository_list = self.client.call('repository.list', self.name)
    for (account_name, repository_name) in repository_list:
      yield dydra.Repository(self.name + '/' + repository_name, client=self.client)
