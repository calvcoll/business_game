import time

class Timer:
  def __init__(self, seconds):
    self.initialTime = int(round(time.time()))
    self.time_to_wait = self.initialTime + seconds

  def isFinished(self):
    if (self.time_to_wait - int(round(time.time()))> 0):
      return False
    return True
