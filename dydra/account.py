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
    return dydra.Repository(self.name + '/' + str(key))
