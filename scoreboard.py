from __future__ import print_function

class ScoreBoard:

    def __init__(self):

        self.scoreBoard = []

    def getTopTen(self, number=10):
        if number > len(self.scoreBoard):
          number = len(self.scoreBoard)
        sorted(self.scoreBoard, key = lambda x: int(x[1]))
        return self.scoreBoard[0:number]

    def loadScoreBoard(self):

        scoreBoard_file = open("scoreboard.txt", "r")

        for players in scoreBoard_file:
            players = players.rstrip("\n")
            players = players.split("|")
            self.scoreBoard.append(players)

        scoreBoard_file.close()

        return self.scoreBoard

    def saveScoreBoard(self):

        scoreBoard_file = open("scoreboard.txt", "w")

        for player in self.scoreBoard:
            print(player[0] + "|" + player[1], file = scoreBoard_file)

        scoreBoard_file.close()

    def addHighScore(self,playerName,playerScore):

        self.player = [playerName,str(playerScore)]
        self.highScoreAdded = False

        for x in range (5):

            if (playerScore >= int(self.scoreBoard[x][1]) and (self.highScoreAdded == False)):

                self.scoreBoard[x] = self.player
                self.saveScoreBoard()
                self.highScoreAdded = True
