class ScoreBoard:

    def __init__(self):

        self.scoreBoard = []

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

          

