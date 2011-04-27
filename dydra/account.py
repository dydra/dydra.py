import dydra

##
# Represents a Dydra.com user account.
#
# @see http://docs.dydra.com/sdk/python
class Account(dydra.Resource):
  """Represents a Dydra.com user account."""

  ##
  # (Attribute) The account name.
  name = None

  ##
  # @param name A valid account name.
  def __init__(self, name, **kwargs):
    self.name = str(name)
    super(Account, self).__init__(self.name, **kwargs)

  ##
  # @return A string representation of this object.
  def __repr__(self):
    return "dydra.Account('%s')" % (self.name)

  ##
  # Returns a particular repository belonging to this account.
  #
  # @param  key A valid repository name.
  # @return A repository.
  def __getitem__(self, key):
    return dydra.Repository(self.name + '/' + str(key), client=self.client)

  ##
  # Iterates the repositories belonging to this account.
  #
  # @return An iterator.
  def __iter__(self):
    repository_list = self.client.call('repository.list', self.name)
    for (account_name, repository_name) in repository_list:
      yield dydra.Repository(self.name + '/' + repository_name, client=self.client)
