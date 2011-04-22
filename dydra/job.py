import dydra
from time import sleep

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
    return self.client.call('job.done', self.uuid)

  def status(self):
    return self.client.call('job.status', self.uuid)

  def wait(self, **kwargs):
    delay = 0.5 # seconds
    if kwargs.has_key('delay'):
      delay = float(kwargs['delay'])
    while not self.is_done():
      sleep(delay)
    return self

  def abort(self):
    self.client.call('job.abort', self.uuid)
    return self
