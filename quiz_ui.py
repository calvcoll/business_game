import pygame
import questions
import scoreboard
import timer
import random

def merge(*lists):
    merged = []
    for element in lists:
        merged.extend(element)
    return merged

def textCentre(x,y,width,text,margin):
    textpos = text.get_rect()
    textx = width/2 - tuple(textpos)[2]/2
    screen.blit(text, (x + textx, y + margin))

class TextBox:
    def __init__(self,x,y,w,h,colour,text,textColour,font,centre,objId):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colour = colour
        self.text = text
        self.textColour = textColour
        self.font = font
        self.centre = centre
        self.objId = objId
        self.margin = 10
        self.visible = True

    def isClicked(self):
        if pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.w and pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[1] < self.y + self.h and self.visible:
            #print(self.objId + " clicked")
            return True
        else:
            return False

    def render(self):
        pygame.draw.rect(screen,self.colour,[self.x,self.y,self.w,self.h])
        text = self.font.render(self.text, 1, self.textColour)
        if self.centre:
            textCentre(self.x,self.y,self.w,text,self.margin)
        else:
            screen.blit(text, (self.x + self.margin, self.y + self.margin))

class OptionButton:
    def __init__(self,x,y,label,text,objId,q):
        self.x = x
        self.y = y
        self.w = 250
        self.h = 50
        self.label = label
        self.text = text
        self.objId = objId
        self.colour = colour_btn1
        self.visible = True
        if label[0].lower() == qList[q].get_correct_answer():
            self.correct = True
        else:
            self.correct = False

    def isClicked(self):
        if pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.w and pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[1] < self.y + self.h and self.visible:
            #print(self.objId + " clicked")
            return True
        else:
            return False

    def render(self):
        TextBox(self.x,self.y,self.h,self.h,colour_btn2,self.label,colour_btn1,font2,False,"").render()
        TextBox(self.x+self.h,self.y,self.w-self.h,self.h,self.colour,self.text,colour_btn2,font2,False,"").render()

class ScoreBoard:
    def __init__(self,x,y,columnWidth1,columnWidth2,rowHeight,padding,font,fontColour,boxColour,scoreList,objId):
        self.x = x
        self.y = y
        self.cw1 = columnWidth1
        self.cw2 = columnWidth2
        self.rh = rowHeight
        self.pad = padding
        self.font = font
        self.fontColour = fontColour
        self.boxColour = boxColour
        self.scoreList = scoreList
        self.objId = objId
        self.visible = True
        self.names = [TextBox(self.x,self.y + x*self.rh + x*padding,self.cw1,self.rh,colour_btn1,self.scoreList[x][0],colour_bg,font2,False,"") for x in range(len(scoreList))]
        self.scores = [TextBox(self.x + self.cw1 + padding,self.y + x*self.rh + x*padding,self.cw2,self.rh,colour_btn1,str(self.scoreList[x][1]),colour_bg,font2,False,"") for x in range(len(scoreList))]

    def isClicked(self):
        pass

    def render(self):
        for name in self.names:
            name.render()
        for score in self.scores:
            score.render()

def getRenderQueue():
    rq = []
    for obj in options:
        rq.append(obj)

    for obj in textBoxes:
        rq.append(obj)

    for obj in buttons:
        rq.append(obj)
    return rq

def reset():
    pygame.init()

    global font1
    font1 = pygame.font.SysFont("arial", 32)
    global font2
    font2= pygame.font.SysFont("arial", 24)
    global font3
    font3 = pygame.font.SysFont("arial", 24, True)
    global font4
    font4 = pygame.font.SysFont("arial", 16)
    global colour_btn1
    colour_btn1 = (255,255,255)
    global colour_btn2
    colour_btn2 = (209,3,115)
    global colour_bg
    colour_bg = (158, 171, 5)
    global colour_black
    colour_black = (0,0,0)
    global colour_correct
    colour_correct = (0,255,0)
    global colour_incorrect
    colour_incorrect = (255,0,0)

    global screen

    global game_name_caption
    game_name_caption = "The Quiz of Quizzicalness"

    screen = pygame.display.set_mode([650,450])
    pygame.display.set_caption(game_name_caption)

    global options
    global buttons
    global textBoxes

    options = []
    buttons = [
        TextBox(95,295,150,45,colour_btn2,"Help",colour_btn1,font3,True,"help"),
        TextBox(250,225,150,45,colour_btn2,"Play",colour_btn1,font3,True,"play"),
        TextBox(405,295,150,45,colour_btn2,"High Scores",colour_btn1,font3,True,"highscores"),
        TextBox(250,365,150,45,colour_btn2,"Exit",colour_btn1,font3,True,"quit")
    ]

    textBoxes = [
        TextBox(125,100,400,54,colour_btn1,game_name_caption,colour_btn2,font1,True,"title"),
    ]

    global renderQueue
    renderQueue = getRenderQueue()

    global done
    done = False

    global answered
    answered = False

    global helptext
    helptext = open('help.txt','r').read()

    qi = questions.QuestionImporter()

    global qList
    qList = qi.import_random_questions(15)

    global score
    score = 0

    global scores
    global board
    board = scoreboard.ScoreBoard()
    board.loadScoreBoard()
    scores = board.getTopTen(5)

    global q
    q = -1

    #print(len(qList))


def getRenderObject(objectId):
    for obj in renderQueue:
        if obj.objId == objectId:
            return obj

reset()

while not done:
    screen.fill(colour_bg)

    if q >= 0:
        getRenderObject("score").text = "Score: " + str(score)
        if t.getTime() >= 0:
            getRenderObject("timer").text = str(t.getTime())
        elif not answered:
            answered = True
            getRenderObject("5050").visible = False
            getRenderObject("double").visible = False
            getRenderObject("timer").visible = False
            renderQueue.append(TextBox(275,225,100,50,colour_btn1,"Next",colour_btn2,font2,True,"next"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in options:
                if button.isClicked() and not answered:
                    answered = True
                    getRenderObject("5050").visible = False
                    getRenderObject("double").visible = False
                    getRenderObject("timer").visible = False
                    renderQueue.append(TextBox(275,225,100,50,colour_btn1,"Next",colour_btn2,font2,True,"next"))
                    if button.correct:
                        button.colour = colour_correct
                        if fifty:
                            score += 5
                        elif double:
                            score += 20
                        else:
                            score += 10
                    else:
                        button.colour = colour_incorrect
                        if fifty:
                            score -= 10
                        elif double:
                            score -= 20
            for button in renderQueue:
                if button.isClicked():
                    if button.objId == "quit":
                        #renderQueue = []
                        done = True
                    if button.objId == "play":
                        q = 0
                        t = timer.Timer(10)
                        fifty = False
                        double = False
                        options = [
                            OptionButton(50,300,"A)",qList[q].get_answers()[0],"opt1",q),
                            OptionButton(50,375,"B)",qList[q].get_answers()[1],"opt2",q),
                            OptionButton(350,300,"C)",qList[q].get_answers()[2],"opt3",q),
                            OptionButton(350,375,"D)",qList[q].get_answers()[3],"opt4",q)
                        ]
                        buttons = [
                            TextBox(25,0,75,50,colour_btn1,"Quit",colour_btn2,font2,True,"quit"),
                            TextBox(125,225,100,50,colour_btn1,"50/50",colour_btn2,font2,True,"5050"),
                            TextBox(275,225,100,50,colour_btn1,"2x",colour_btn2,font2,True,"double")
                        ]
                        textBoxes = [
                            TextBox(475,0,150,50,colour_btn1,"",colour_btn2,font2,False,"score"),
                            TextBox(25,75,600,125,colour_bg,qList[q].get_title(),colour_btn1,font2,False,"questionText"),
                            TextBox(425,225,100,50,colour_btn1,"10",colour_btn2,font2,True,"timer")
                        ]
                        renderQueue = getRenderQueue()
                    if button.objId == "next":
                        t = timer.Timer(10)
                        if q < len(qList)-1:
                            q += 1
                            fifty = False
                            double = False
                            answered = False
                            options = [
                                OptionButton(50,300,"A)",qList[q].get_answers()[0],"opt1",q),
                                OptionButton(50,375,"B)",qList[q].get_answers()[1],"opt2",q),
                                OptionButton(350,300,"C)",qList[q].get_answers()[2],"opt3",q),
                                OptionButton(350,375,"D)",qList[q].get_answers()[3],"opt4",q)
                            ]
                            buttons = [
                                TextBox(25,0,75,50,colour_btn1,"Quit",colour_btn2,font2,True,"quit"),
                                TextBox(125,225,100,50,colour_btn1,"50/50",colour_btn2,font2,True,"5050"),
                                TextBox(275,225,100,50,colour_btn1,"2x",colour_btn2,font2,True,"double")
                            ]
                            textBoxes = [
                                TextBox(475,0,150,50,colour_btn1,"",colour_btn2,font2,False,"score"),
                                TextBox(25,75,600,125,colour_bg,qList[q].get_title(),colour_btn1,font2,False,"questionText"),
                                TextBox(425,225,100,50,colour_btn1,"10",colour_btn2,font2,True,"timer")
                            ]
                            renderQueue = getRenderQueue()
                        else:
                            q = -1
                            options = []
                            buttons = [
                                TextBox(475,400,150,50,colour_btn1,"Back",colour_btn2,font2,False,"back")
                            ]
                            textBoxes = [
                                TextBox(25,25,600,350,colour_bg,"End of quiz!",colour_btn1,font2,False,""),
                                TextBox(25,75,600,350,colour_bg,"Your final score: " + str(score),colour_btn1,font2,False,""),
                                TextBox(25,125,600,350,colour_bg,"Enter your name in the terminal to submit your score.",colour_btn1,font2,False,"")
                            ]
                            renderQueue = getRenderQueue()
                            for button in renderQueue:
                                if button.visible:
                                    button.render()
                            pygame.display.update()
                            name = raw_input("Enter your name: ")
                            board.addHighScore(name,score)
                            pygame.event.set_grab(True)
                            pygame.event.set_grab(False)
                    if button.objId == "help":
                        options = []
                        buttons = [
                            TextBox(475,400,150,50,colour_btn1,"Back",colour_btn2,font2,False,"back")
                        ]
                        textBoxes = []
                        newY = 25
                        add = 25
                        for text in helptext.split('\n'):
                            textBoxes.append(TextBox(25,newY,600,newY,colour_bg,text,colour_btn1,font4,False,""))
                            newY += add * 1.5
                        renderQueue = getRenderQueue()
                    if button.objId == "back":
                        reset()
                    if button.objId == "highscores":
                        options = []
                        buttons = [
                            TextBox(475,400,150,50,colour_btn1,"Back",colour_btn2,font2,False,"back")
                        ]
                        textBoxes = [
                            ScoreBoard(25,25,500,100,50,5,font2,colour_bg,colour_btn1,scores,"scoreboard")
                        ]
                        renderQueue = getRenderQueue()
                    if button.objId == "5050" and not answered and not double:
                        button.colour = colour_correct
                        fifty = True
                        r1 = random.randint(0,3)
                        r2 = random.randint(0,3)
                        while options[r1].correct or options[r2].correct or r1 == r2:
                            r1 = random.randint(0,3)
                            r2 = random.randint(0,3)
                        options[r1].visible = False
                        options[r2].visible = False
                    if button.objId == "double" and not answered and not fifty:
                        button.colour = colour_correct
                        double = True
                    ###remove this###
                    #if button.objId == "score":
                        #reset()
                    ###///////////###


            
    for button in renderQueue:
        if button.visible:
            button.render()

    pygame.display.update()

pygame.quit()
