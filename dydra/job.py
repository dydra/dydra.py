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
    return self.status() == 'pending'

  def is_running(self):
    return self.status() == 'running'

  def is_completed(self):
    return self.status() == 'completed'

  def is_failed(self):
    return self.status() == 'failed'

  def is_aborted(self):
    return self.status() == 'aborted'

  def is_done(self):
    status = self.status()
    return status == 'completed' or status == 'failed' or status == 'aborted'

  def status(self):
    self.client.call('job.status', self.uuid)

  def wait(self, **kwargs):
    raise NotImplementedError

  def abort(self):
    raise NotImplementedError
