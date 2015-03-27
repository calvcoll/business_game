import pygame
import questions

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
        if pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.w and pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[1] < self.y + self.h:
            print(self.objId + " clicked")
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
        if pygame.mouse.get_pos()[0] > self.x and pygame.mouse.get_pos()[0] < self.x + self.w and pygame.mouse.get_pos()[1] > self.y and pygame.mouse.get_pos()[1] < self.y + self.h:
            print(self.objId + " clicked")
            return True
        else:
            return False

    def render(self):
        TextBox(self.x,self.y,self.h,self.h,colour_btn2,self.label,colour_btn1,font2,False,"").render()
        TextBox(self.x+self.h,self.y,self.w-self.h,self.h,self.colour,self.text,colour_btn2,font2,False,"").render()

def getRenderQueue():
    rq = []
    for obj in options:
        rq.append(obj)

    for obj in buttons:
        rq.append(obj)

    for obj in textBoxes:
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
    screen = pygame.display.set_mode([650,450])
    pygame.display.set_caption("game")

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
        TextBox(125,100,400,54,colour_btn1,"The Quiz of Quizicalness",colour_btn2,font1,True,"title"),
    ]

    global renderQueue
    renderQueue = getRenderQueue()

    global done
    done = False

    global answered
    answered = False

    qi = questions.QuestionImporter()

    global qList
    #not working
    #qList = qi.import_random_questions(1)
    qList = [questions.Question({'title' : "question?",
                'answer' : "b", 'a1' : "incorrect",
                'a2' : "correct", 'a3' : "incorrect",
                'a4' : "incorrect"})]

def getRenderObject(objectId):
    for obj in renderQueue:
        if obj.objId == objectId:
            return obj

reset()

while not done:
    screen.fill(colour_bg)

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
                    if button.correct:
                        button.colour = colour_correct
                    else:
                        button.colour = colour_incorrect
            for button in renderQueue:
                if button.isClicked():
                    if button.objId == "quit":
                        #renderQueue = []
                        done = True
                    if button.objId == "play":
                        q = 0
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
                            TextBox(475,0,150,50,colour_btn1,"Score: 0",colour_btn2,font2,False,"score"),
                            TextBox(25,75,600,125,colour_bg,qList[q].get_title(),colour_btn1,font2,False,"questionText"),
                            TextBox(425,225,100,50,colour_btn1,"10",colour_btn2,font2,True,"timer")
                        ]
                        renderQueue = getRenderQueue()
                    if button.objId == "help":
                        options = []
                        buttons = []
                        textBoxes = []
                        renderQueue = getRenderQueue()
                    if button.objId == "highscores":
                        options = []
                        buttons = []
                        textBoxes = []
                        renderQueue = getRenderQueue()
                    if button.objId == "5050" and not answered:
                        button.colour = colour_correct
                    if button.objId == "double" and not answered:
                        button.colour = colour_correct
                    ###remove this###
                    if button.objId == "score":
                        reset()
                    ###///////////###

    for button in renderQueue:
        if button.visible:
            button.render()

    pygame.display.update()

pygame.quit()
