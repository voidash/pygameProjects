import pygame
import os

#colors

black = (0,0,0)
white= (255,255,255)

walkRight = [pygame.image.load('assets/R1.png'), pygame.image.load('assets/R2.png'), pygame.image.load('assets/R3.png'), pygame.image.load('assets/R4.png'), pygame.image.load('assets/R5.png'), pygame.image.load('assets/R6.png'), pygame.image.load('assets/R7.png'), pygame.image.load('assets/R8.png'), pygame.image.load('assets/R9.png')]
walkLeft = [pygame.image.load('assets/L1.png'), pygame.image.load('assets/L2.png'), pygame.image.load('assets/L3.png'), pygame.image.load('assets/L4.png'), pygame.image.load('assets/L5.png'), pygame.image.load('assets/L6.png'), pygame.image.load('assets/L7.png'), pygame.image.load('assets/L8.png'), pygame.image.load('assets/L9.png')]
bg = pygame.image.load('assets/bg.jpg')
char = pygame.image.load('assets/standing.png')

pygame.init()
width_ = 852
height_ = 480
screen = pygame.display.set_mode((width_,height_))

pygame.display.set_caption("Revision")


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width= width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = True
        self.right = False
        self.walkCount = 0
        self.jumpFactor = 10
        self.jumpCount = self.jumpFactor
        self.standing = True


    def draw(self,screen):
        if self.walkCount+1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3],[self.x,self.y])
                self.walkCount+=1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],[self.x,self.y])
                self.walkCount +=1
            else:
                if self.right:
                    win.blit(walkRight[0],(self.x,self.y))
                elif self.left:
                    win.blit(walkLeft[0],(self.x,self.y))

gameExit = False

while not gameExit:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            gameExit = True
        screen.fill(white)
#method A
        keys = pygame.key.get_pressed()






        pygame.draw.rect(screen,black,(0,0,10,10))
        pygame.display.update()
