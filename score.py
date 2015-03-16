class Score:

  def __init__(self):
    self.score = 0

  def setScore(self,correct,usedx2,used5050):
    if correct:
      if usedx2:
        self.score += 20
      elif used5050:
        self.score += 5
      else:
        self.score += 10
    else:
      if usedx2:
        self.score -= 20
      elif used5050:
        self.score -= 10
      else:
        self.score += 0        

  def getScore(self):
    return self.score
