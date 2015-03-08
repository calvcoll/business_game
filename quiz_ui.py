import pygame

class TextBox:
    def __init__(self,x,y,w,h,colour,text,textColour,font):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colour = colour
        self.text = text
        self.textColour = textColour
        self.font = font
        self.margin = 10

    def render(self):
        pygame.draw.rect(screen,self.colour,[self.x,self.y,self.w,self.h])
        text = self.font.render(self.text, 1, self.textColour)
        screen.blit(text, (self.x + self.margin, self.y + self.margin))

class OptionButton:
    def __init__(self,x,y,label,text,correct):
        self.x = x
        self.y = y
        self.w = 250
        self.h = 50
        self.label = label
        self.text = text
        self.correct = correct
        self.colour = white

    def render(self):
        TextBox(self.x,self.y,self.h,self.h,pink,self.label,white,font2).render()
        TextBox(self.x+self.h,self.y,self.w-self.h,self.h,self.colour,self.text,pink,font2).render()

pygame.init()

font1 = pygame.font.SysFont("arial", 32)
font2 = pygame.font.SysFont("arial", 24)
white = (255,255,255)
pink = (209,3,115)
green = (158, 171, 5)
black = (0,0,0)

screen = pygame.display.set_mode([650,450])
pygame.display.set_caption("game")

done = False

options = [
    OptionButton(50,300,"A)","Option 1",False),
    OptionButton(50,375,"B)","Option 2",True),
    OptionButton(350,300,"C)","Option 3",False),
    OptionButton(350,375,"D)","Option 4",False)
]

renderQueue = [
    TextBox(25,0,75,50,white,"Quit",pink,font2),
    TextBox(475,0,150,50,white,"Score: 0",pink,font2),
    TextBox(25,75,600,125,white,"Example question?",pink,font2),
    TextBox(125,225,100,50,white,"50/50",pink,font2),
    TextBox(425,225,100,50,white,"10",pink,font2),
    options[0],
    options[1],
    options[2],
    options[3]
]

while not done:
    screen.fill(green)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in options:
                if pygame.mouse.get_pos()[0] > button.x and pygame.mouse.get_pos()[0] < button.x + button.w and pygame.mouse.get_pos()[1] > button.y and pygame.mouse.get_pos()[1] < button.y + button.h:
                    print(button.text + " clicked")
                    if button.correct:
                        button.colour = (0,255,0)
                    else:
                        button.colour = (255,0,0)
    
    for button in renderQueue:
        button.render()

    pygame.display.update()

pygame.quit()
