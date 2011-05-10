import dydra
from time import sleep

##
# Represents a Dydra.com job.
#
# @see http://docs.dydra.com/sdk/python
class Job(dydra.Resource):
  """Represents a Dydra.com job."""

  STATUS_UNKNOWN   = 'unknown'
  STATUS_PENDING   = 'pending'
  STATUS_RUNNING   = 'running'
  STATUS_COMPLETED = 'completed'
  STATUS_FAILED    = 'failed'
  STATUS_ABORTED   = 'aborted'

  ##
  # (Attribute) The job UUID.
  uuid = None

  ##
  # Initializes the job instance.
  #
  # @param uuid A valid job UUID.
  def __init__(self, uuid, **kwargs):
    super(Job, self).__init__(self.uuid, **kwargs) # FIXME
    self.uuid = str(uuid)

  ##
  # Returns a string representation of the job UUID.
  #
  # @return A string representation of this object.
  def __repr__(self):
    return "dydra.Job('%s')" % (self.uuid)

  ##
  # Returns `True` if this job is currently pending to run.
  def is_pending(self):
    return self.status() == STATUS_PENDING

  ##
  # Returns `True` if this job is currently running.
  def is_running(self):
    return self.status() == STATUS_RUNNING

  ##
  # Returns `True` if this job has already completed.
  def is_completed(self):
    return self.status() == STATUS_COMPLETED

  ##
  # Returns `True` if this job failed for some reason.
  def is_failed(self):
    return self.status() == STATUS_FAILED

  ##
  # Returns `True` if this job was aborted for any reason.
  def is_aborted(self):
    return self.status() == STATUS_ABORTED

  ##
  # Returns `True` if this job has completed or was aborted, and
  # `False` if it's currently pending or running.
  def is_done(self):
    return self.client.call('job.done', self.uuid)

  ##
  # Returns the current status of this job.
  def status(self):
    return self.client.call('job.status', self.uuid)

  ##
  # Waits until this job is done.
  def wait(self, **kwargs):
    # TODO: timeout support
    delay = 0.5 # seconds
    if kwargs.has_key('delay'):
      delay = float(kwargs['delay'])
    while not self.is_done():
      sleep(delay)
    return self

  ##
  # Aborts this job if it is currently pending or running.
  def abort(self):
    self.client.call('job.abort', self.uuid)
    return self
