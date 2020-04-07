import pygame as pg 
from settings import *

class tile(pg.sprite.Sprite):
    def __init__(self,g,rowPos,colPos):
        pg.sprite.Sprite.__init__(self,g.tiles)
        self.g = g
        
        #create image
        self.image = pg.Surface((self.g.tilesize*3/4,self.g.tilesize*3/4)) #rectangular
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (rowPos+self.g.tilesize*1/2,colPos+self.g.tilesize*1/2)
        self.alive = True
    
    def update(self): #condition actually checks if tile dies or not
        if self.alive==False:
            self.g.tiles.remove(self)
