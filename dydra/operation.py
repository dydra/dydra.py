import dydra
from time import sleep

##
# Represents a Dydra.com operation.
#
# @see http://docs.dydra.com/sdk/python
class Operation(dydra.Resource):
  """Represents a Dydra.com operation."""

  STATUS_UNKNOWN   = 'unknown'
  STATUS_PENDING   = 'pending'
  STATUS_RUNNING   = 'running'
  STATUS_COMPLETED = 'completed'
  STATUS_FAILED    = 'failed'
  STATUS_ABORTED   = 'aborted'

  ##
  # (Attribute) The operation UUID.
  uuid = None

  ##
  # Initializes the operation instance.
  #
  # @param uuid A valid operation UUID.
  def __init__(self, uuid, **kwargs):
    super(Operation, self).__init__(self.uuid, **kwargs) # FIXME
    self.uuid = str(uuid)

  ##
  # Returns a string representation of the operation UUID.
  #
  # @return A string representation of this object.
  def __repr__(self):
    return "dydra.Operation('%s')" % (self.uuid)

  ##
  # Returns `True` if this operation is currently pending to run.
  def is_pending(self):
    return self.status() == STATUS_PENDING

  ##
  # Returns `True` if this operation is currently running.
  def is_running(self):
    return self.status() == STATUS_RUNNING

  ##
  # Returns `True` if this operation has already completed.
  def is_completed(self):
    return self.status() == STATUS_COMPLETED

  ##
  # Returns `True` if this operation failed for some reason.
  def is_failed(self):
    return self.status() == STATUS_FAILED

  ##
  # Returns `True` if this operation was aborted for any reason.
  def is_aborted(self):
    return self.status() == STATUS_ABORTED

  ##
  # Returns `True` if this operation has completed or was aborted, and
  # `False` if it's currently pending or running.
  def is_done(self):
    return self.client.call('operation.done', self.uuid)

  ##
  # Returns the current status of this operation.
  def status(self):
    return self.client.call('operation.status', self.uuid)

  ##
  # Waits until this operation is done.
  def wait(self, **kwargs):
    # TODO: timeout support
    delay = 0.5 # seconds
    if kwargs.has_key('delay'):
      delay = float(kwargs['delay'])
    while not self.is_done():
      sleep(delay)
    return self

  ##
  # Aborts this operation if it is currently pending or running.
  def abort(self):
    self.client.call('operation.abort', self.uuid)
    return self
