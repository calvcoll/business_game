import pygame.time

class Timer():
  def __init__(seconds):
    this.initialTime = pygame.time.get_time()
    this.time_to_wait = this.initialTime + (seconds * 60)

  def isFinished():
    if (this.initialTime - this.time_to_wait > 0) return False
    else return True
