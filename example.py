import pygame
import random

pygame.init()

clock = pygame.time.Clock()

class Window:
    def __init__(self,w,h,caption):
        self.screen = pygame.display.set_mode([w,h])
        pygame.display.set_caption(caption)

    def refresh(self):
        self.screen.fill((0, 0, 0))

class Player:
    def __init__(self,w,h,x,y,spd):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.speed = spd

    def moveRight(self):
        self.x += self.speed

    def moveLeft(self):
        self.x -= self.speed

    def moveDown(self):
        self.y += self.speed

    def moveUp(self):
        self.y -= self.speed

w1 = Window(650,450,"game")

p1 = Player(16,16,64,64,8)

done = False

while not done:

    clock.tick(60)

    w1.refresh()
    
    #keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        p1.x += p1.speed

    if keys[pygame.K_a]:
        p1.x -= p1.speed

    if keys[pygame.K_s]:
        p1.y += p1.speed

    if keys[pygame.K_w]:
        p1.y -= p1.speed

    pygame.draw.rect(w1.screen,[255,255,255],[p1.x,p1.y,p1.w,p1.h])

    pygame.display.flip()

pygame.quit()
