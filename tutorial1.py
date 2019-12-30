import pygame
import sys
pygame.init()
window=pygame.display.set_mode([400,400])
pygame.display.set_caption("najau na malai chodi aakha modi")
x_pos=0
y_pos=0
Co_ordinates=[]
ConnectorListInitialPos=[]
ConnectorListFinalPos=[]
gameLoop = True
drawConnector=False
clock = pygame.time.Clock()
while gameLoop:
   if not drawConnector:
       window.fill((255,255,255))
   clock.tick(100)
   for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit()
       eventKeys=pygame.key.get_pressed()

       if event.type == pygame.MOUSEBUTTONDOWN:
           #print(pygame.mouse.get_pos())
           Co_ordinates = pygame.mouse.get_pos()
           print(Co_ordinates)
           drawConnector=True
       if event.type == pygame.MOUSEBUTTONUP:
           drawConnector=False
           finalPosition=pygame.mouse.get_pos()
           ConnectorListInitialPos.append(Co_ordinates)
           ConnectorListFinalPos.append(finalPosition)
       if drawConnector:
           currentPosition=pygame.mouse.get_pos()
           window.fill((255,255,255))
           pygame.draw.line(window,(255,255,0),Co_ordinates,currentPosition,5)



   pygame.draw.rect(window,(255,0,0),[x_pos,y_pos,50,50])
   for x,y in zip(ConnectorListInitialPos,ConnectorListFinalPos):
       pygame.draw.line(window,(255,0,0),x,y,5)



   pygame.display.update()



# checking for a mouse event
# a line is drawn from the click down till click up
