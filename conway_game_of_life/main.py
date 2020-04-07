import pygame as pg 
import random
import os
from settings import *
from tiles import *
import time

""" 
python game of life

"""


class gameOfLife:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(WINDOW)
        pg.display.set_caption("Game of Life")
        self.running = True
        self.tile_data=[]
        self.timeNow = 0
        self.importFile()
        self.run()
        #conway logic
        
        

    def importFile(self):
        file = os.path.dirname(__file__)
        with open(os.path.join(file,'setup.txt'),'rt') as f:
            for line in f:
                a = list(line)
                if a != []:
                    if '\n' in a:
                        a.remove('\n')
                self.tile_data.append(a)
        
        #check if the file is square or not.
        if len(self.tile_data)-1 != len(self.tile_data[0]):
            print(len(self.tile_data) ," ",len(self.tile_data[0]))

        self.tile_change=list()
        self.tilesize = WIDTH//(len(self.tile_data))
        self.tile_instance_data =list()
        for x in range(0,len(self.tile_data[0])):
            self.tile_change.append(list())
            self.tile_instance_data.append(list())
            for y in range(0,len(self.tile_data[0])):
                self.tile_change[x].append(False)
                self.tile_instance_data[x].append(0)


    def run(self):
        self.tiles = pg.sprite.Group()
        self.clock = pg.time.Clock()
        while self.running:
            self.update()
            self.event()
            self.draw()
#conway game of life logic
    def conwayLogic(self,row,col,size):
        startPointX = row - 1 if row != 0 else 0
        startPointY = col - 1 if col != 0 else 0
        Neighbours = 0
        endPointX = row +2 if row+1 != size else row
        endPointY = col +2 if col+1 != size else col
        for x in range(startPointX,endPointX):
            for y in range(startPointY,endPointY):
                if self.tile_data[x][y]=='1':
                    Neighbours+=1
        #print("the neighbours for ({},{}) is {}".format(row,col,Neighbours))
        ownState = self.tile_data[row][col] 
        #print(ownState)
        #main conway logic
        if ownState == '1':
            Neighbours = Neighbours - 1
            if Neighbours > 3:
                self.tile_change[row][col]=True
            elif Neighbours < 2:
                self.tile_change[row][col]=True
        elif ownState == '0':
            if Neighbours == 3:
                self.tile_change[row][col]=True
    


    def checkCellState(self):
        for row,i in enumerate(self.tile_data):
            for col,j in enumerate(i):
                if j == '1':
                    if self.tile_instance_data[row][col] == 0:
                        self.tile_instance_data[row][col] = tile(self,col*self.tilesize,row*self.tilesize)
                        
                elif j == '0':
                    if self.tile_instance_data[row][col] != 0:
                        self.tile_instance_data[row][col].alive = False
                        self.tile_instance_data[row][col]=0
        size = len(self.tile_data[0])
        for x in range(0,size):
            for y in range(0,size):
                self.conwayLogic(x,y,size)
        
        for x in range(0,size):
            for y in range(0,size):
                if self.tile_change[x][y] == True:
                    self.tile_data[x][y] = '1' if self.tile_data[x][y] =='0' else '0'
                    self.tile_change[x][y] = False

        
                    

        

        
    
        
    def update(self):
        self.clock.tick(FPS)
        
        millisNow  = lambda: int(round(time.time()))
        self.timeNow = self.timeNow or millisNow()
        if(self.timeNow+1<millisNow()):
            self.timeNow = 0
            print("now is the check cell state")
            
        self.checkCellState()
        self.tiles.update()
        
    def event(self):
        for events in pg.event.get():
            if events.type == pg.QUIT:
                self.running = False

    def draw_grids(self,tilesize):
        #according to file length draw grids to accomodate tile size
        for x in range(0,WIDTH,tilesize): #since game window is square only one loop needed 
            pg.draw.line(self.window,LIGHTGREY,(x,0),(x,WIDTH))
            pg.draw.line(self.window,LIGHTGREY,(0,x),(HEIGHT,x))



    def draw(self):
        self.window.fill(BGCOLOR)
        self.draw_grids(self.tilesize)
        self.tiles.draw(self.window)
        pg.display.flip()

    def condition(self):
        pass

g = gameOfLife()

    
    