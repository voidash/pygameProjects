import pygame
import sys
pygame.init()

window=pygame.display.set_mode((800,800))
pygame.display.set_caption("And Gate")
x=100
y=100
gameExit = False
while not gameExit:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
            gameExit=True
    window.fill((255,255,255))
    pygame.draw.line(window,(255,0,0),(126+x,98+y),(126+x,262+y),5)
    #pygame.draw.arc(window,(255,0,0),[86+x,98+y,110,167],4.55,8,5) for or gates
    pygame.draw.line(window,(255,0,0),(126+x,262+y),(285+x,262+y),5)
    pygame.draw.line(window,(255,0,0),(126+x,98+y),(285+x,98+y),5)
    pygame.draw.arc(window,(255,0,0),[236+x,98+y,110,167],4.55,8,5)

    pygame.display.update()
