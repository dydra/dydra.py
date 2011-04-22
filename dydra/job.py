import dydra

class Job(dydra.Resource):
  """A running job/task on Dydra.com."""

  uuid = None

  def __init__(self, uuid, **kwargs):
    self.uuid = str(uuid)
    super(Job, self).__init__(self.uuid, **kwargs) # FIXME

  def __repr__(self):
    return "dydra.Job('%s')" % (self.uuid)

  def is_pending(self):
    raise NotImplementedError

  def is_running(self):
    raise NotImplementedError

  def is_done(self):
    raise NotImplementedError

  def is_completed(self):
    raise NotImplementedError

  def is_aborted(self):
    raise NotImplementedError

  def status(self):
    raise NotImplementedError

  def wait(self, **kwargs):
    raise NotImplementedError

  def abort(self):
    raise NotImplementedError
