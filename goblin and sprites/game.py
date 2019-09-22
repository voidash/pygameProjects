import pygame
import os
import time
pygame.init()
width_ = 852
height_ = 480
win = pygame.display.set_mode((width_,height_))

font= pygame.font.SysFont('Times New Roman',100)



pygame.display.set_caption("game")

walkRight = [pygame.image.load('assets/R1.png'), pygame.image.load('assets/R2.png'), pygame.image.load('assets/R3.png'), pygame.image.load('assets/R4.png'), pygame.image.load('assets/R5.png'), pygame.image.load('assets/R6.png'), pygame.image.load('assets/R7.png'), pygame.image.load('assets/R8.png'), pygame.image.load('assets/R9.png')]
walkLeft = [pygame.image.load('assets/L1.png'), pygame.image.load('assets/L2.png'), pygame.image.load('assets/L3.png'), pygame.image.load('assets/L4.png'), pygame.image.load('assets/L5.png'), pygame.image.load('assets/L6.png'), pygame.image.load('assets/L7.png'), pygame.image.load('assets/L8.png'), pygame.image.load('assets/L9.png')]
bg = pygame.image.load('assets/bg.jpg')
char = pygame.image.load('assets/standing.png')
clock = pygame.time.Clock()
gameOver = False
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height =height
        self.vel = 5
        self.isJump = False
        self.left = True
        self.right = False
        self.walkCount = 0
        self.jumpFactor = 10
        self.jumpCount = self.jumpFactor
        self.standing = True
        self.hitbox = [self.x+20,self.y+10,28,50]

    def draw(self,win):
        if self.walkCount+1>=27:
            self.walkCount=0

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
        self.hitbox = [self.x+20,self.y+10,28,50]
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)
class projectile():
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8*facing
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

class enemy(object):
    walkRight = [pygame.image.load('assets/R1E.png'), pygame.image.load('assets/R2E.png'), pygame.image.load('assets/R3E.png'), pygame.image.load('assets/R4E.png'), pygame.image.load('assets/R5E.png'), pygame.image.load('assets/R6E.png'), pygame.image.load('assets/R7E.png'), pygame.image.load('assets/R8E.png'), pygame.image.load('assets/R9E.png'), pygame.image.load('assets/R10E.png'), pygame.image.load('assets/R11E.png')]
    walkLeft = [pygame.image.load('assets/L1E.png'), pygame.image.load('assets/L2E.png'), pygame.image.load('assets/L3E.png'), pygame.image.load('assets/L4E.png'), pygame.image.load('assets/L5E.png'), pygame.image.load('assets/L6E.png'), pygame.image.load('assets/L7E.png'), pygame.image.load('assets/L8E.png'), pygame.image.load('assets/L9E.png'), pygame.image.load('assets/L10E.png'), pygame.image.load('assets/L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x,self.end]
        self.walkCount = 0
        self.vel =3
        self.hitbox = [self.x+17,self.y+2,31,57]
        self.health = 40
        self.healthbox=[self.x+10,self.y-40,40,10]
    def draw (self,win):
        self.move(win)
        if self.walkCount +1 >= 33:
            self.walkCount =0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1
        self.hitbox = [self.x+17,self.y+2,31,57]
        self.healthbox = [self.x+10,self.y-40,40,10]
        pygame.draw.rect(win,(255,0,0),[self.x+10,self.y-40,self.health,10])
        pygame.draw.rect(win,(255,0,0),self.healthbox,1)
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        if self.health < 0:
            gameOverText = font.render("Game Over",100,(255,0,0))
            win.blit(gameOverText,[width_//2-200,height_//2-100])


            


    def move(self,win):
        if self.vel > 0:

            if self.x+self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel >self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
    def hit(self):
        print('hit')
        self.health -= 5
        if self.health == 0:
            print("game over")
            gameOver = True









def redrawGameWindow():
    win.blit(bg,(0,0))
    man.draw(win)
    goblin.draw(win)
    #pygame.draw.rect(win,(255,255,255),(x,y,50,100))
    for bullet in bullets:
        bullet.draw(win)
    if gameOver:
        gameOverText = font.render("Game Over",44,(255,255,0))
        win.blit(gameOverText,[0,0])

    pygame.display.update()


goblin = enemy(100,410,64,64,800)

man = player(400,410,64,64)

bullets =[]
#main loop
shootLoop = 0
run =True
while run:
    clock.tick(30)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 5:
        shootLoop = 0


    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

    if goblin.hitbox[0]+goblin.hitbox[2] > man.hitbox[0] and goblin.hitbox[0]+goblin.hitbox[2] < man.hitbox[0]+man.hitbox[2] and man.hitbox[1] > goblin.hitbox[1]:
        print("hit by goblin")
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y +bullet.radius > goblin.hitbox[1]:
            if bullet.x+bullet.radius >goblin.hitbox[0] and bullet.x-bullet.radius<goblin.hitbox[0]+goblin.hitbox[2]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))


        if bullet.x< width_ and bullet.x >0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys= pygame.key.get_pressed()
    if events.type == pygame.KEYDOWN:
        if events.key == pygame.K_SPACE and shootLoop == 0   :
            shootLoop = 1
            if man.left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 10:

                bullets.append(projectile(round(man.x+man.width//2),round(man.y + man.height //2),6,(0,0,0),facing))

    if keys[pygame.K_LEFT] and man.x>=0:
        man.left= True
        man.right= False
        man.x-=man.vel
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x<=width_-man.width-man.vel:
        man.left= False
        man.right = True
        man.x+=man.vel
        man.standing = False

    else:
        man.standing = True

        man.walkCount = 0

    if not(man.isJump):

        if keys[pygame.K_DOWN] and man.y<=height_:
            man.y+=man.vel

        if keys[pygame.K_UP]:
            man.isJump = True
    else:
        if man.jumpFactor >= -man.jumpCount:
            neg = 1
            if man.jumpFactor < 0:
                neg =-1

            man.y -= (man.jumpFactor ** 2)*0.5*neg

            man.jumpFactor -= 1
        else:
            man.isJump = False
            man.jumpFactor = man.jumpCount

    redrawGameWindow()





pygame.quit()
