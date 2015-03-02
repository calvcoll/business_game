import timer
import time
import unittest

class Timer_Test(unittest.TestCase):
  def test_timer(self):
    t = timer.Timer(1)
    self.assertEqual(t.isFinished(), False)
    time.sleep(1)
    self.assertEqual(t.isFinished(), True)
