import pygame
import random

class Question:
    def __init__(self,q,ans1,ans2,ans3,correctAns):
        self.q = q
        self.answers = [ans1,ans2,ans3,correctAns]
        self.buttons = [
            Button(100,200,200,75,self.answers[0],[255,0,0]),
            Button(350,200,200,75,self.answers[1],[0,255,0]),
            Button(100,325,200,75,self.answers[2],[0,0,255]),
            Button(350,325,200,75,self.answers[3],[255,255,0])
        ]

    def render(self):
        text = font1.render(self.q, 1, (0,0,0))
        screen.blit(text, (100, 100))
        for button in self.buttons:
            button.render()

class Button:
    def __init__(self,x,y,w,h,text,colour):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.colour = colour

    def render(self):
        pygame.draw.rect(screen,self.colour,[self.x,self.y,self.w,self.h])
        textRender = font2.render(self.text, 1, (0,0,0))
        screen.blit(textRender, (self.x, self.y))

questions = [
    Question("Example question?","Option 1","Option 2","Option 3","Option 4 (correct)")
]

pygame.init()

font1 = pygame.font.SysFont("monospace", 32)
font2 = pygame.font.SysFont("monospace", 16)

clock = pygame.time.Clock()

screen = pygame.display.set_mode([650,450])
pygame.display.set_caption("game")

done = False

while not done:

    n = 0

    clock.tick(60)

    screen.fill((255, 255, 255))
    
    #keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in questions[n].buttons:
                if pygame.mouse.get_pos()[0] > button.x and pygame.mouse.get_pos()[0] < button.x + button.w and pygame.mouse.get_pos()[1] > button.y and pygame.mouse.get_pos()[1] < button.y + button.h:
                    print(button.text)
                    button.x += 1000

    questions[n].render()

    pygame.display.update()

pygame.quit()
