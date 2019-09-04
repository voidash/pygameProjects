import sys,pygame

pygame.init()

width,height =800,600
size = [width,height]

#setting the screen size
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Elastic collision for calculating value of PI')
#colors
white = (255,255,255)
black=(0,0,0)
purple=(155,17,238)
'''
elastic collision is where both momentum and energy is conserved
here is the basic # IDEA:
you hava two ideal bodies. One with bigger mass m1 = 100kg and another smaller mass m2 =100kg
velocity of bigger mass is u1 and velocity of smaller mass is u2 (before collision)
after collision velocity of bigger mass is v1 and smaller mass is v2
m1u1+m2u2 = m1v1+m2v2(extension of newtons 3rd law)
and
v1 = ((m1-m2)/(m1+m2))*u1 +(2m2/(m1+m2))*u2
v2 = (2m1/(m1+m2))*u1+(m2-m1/m1+m2)*u2
'''

m1,v1=10000,-1 #1st body is moving towards it
m2,v2=1,0 #2nd body is stationary
objectA=[m1,v1]
objectB=[m2,v2]


def truncate(n,place=0):
    multiplier = 10**place #removes decimal part
    return int(n*multiplier)/multiplier


#buffer variable to keep the value initial value of v1 and v2 may be required

#clock for setting the speed
clock = pygame.time.Clock()
horizontal_posA=500
horizontal_posB=100
collision=0
font = pygame.font.SysFont("Times New Roman, Arial",40)
msg = '#collisions '


gameExit= False

while not gameExit:
    clock.tick(100) #limit the while loop for 10 times second
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((255,255,255))
    #drawing the base where elastic collision happen
    pygame.draw.line(screen,black,[0,(height-height/3)],[800,(height-height/3)],3)
    #placing those beautiful rectangles (technically squares are rectangles)
    horizontal_posA = horizontal_posA+objectA[1]
    horizontal_posB = horizontal_posB+objectB[1]
    if (horizontal_posA-(horizontal_posB+m2))<0.1:
        collision=collision+1
        print(collision)

        bufferV1 = objectA[1]
        bufferV2 = objectB[1]
        objectA[1]= ((objectA[0]-objectB[0])/(objectA[0]+objectB[0]))*bufferV1 +(2*objectB[0]/(objectA[0]+objectB[0]))*bufferV2

        objectB[1]= (2*objectA[0]/(objectA[0]+objectB[0]))*bufferV1+((objectB[0]-objectA[0])/(objectA[0]+objectB[0]))*bufferV2

    if horizontal_posB <= 0:
        objectB[1]=-objectB[1]
        collision= collision+1
        print(collision)
    if horizontal_posA <=0:
       pygame.draw.rect(screen,purple,[11,(height-height/3)-150-1,150,150])
       pygame.draw.rect(screen,black,[11,(height-height/3)-150-1,148,148],2)
    else:
       pygame.draw.rect(screen,purple,[horizontal_posA,(height-height/3)-150-1,150,150])
       pygame.draw.rect(screen,black,[horizontal_posA,(height-height/3)-148-1,149,149],2)
    msg = '#collisions '+ str(collision)
    text = font.render(msg,True,black)
    textb = font.render('elastic collision for calculating pi ',True,black)
    pygame.draw.rect(screen,purple,[horizontal_posB,(height-height/3)-10-1,10,10])
    pygame.draw.rect(screen,black,[horizontal_posB,(height-height/3)-8-1,8,8],2)
    screen.blit(textb,(10,10))
    screen.blit(text,(10,100))
    pygame.display.update()
