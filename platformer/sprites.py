from settings import *
import pygame as pg
from random import choice
vec = pg.math.Vector2


class SpriteSheet:
    def __init__(self,filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self,x,y,width,height):
        #image grabbing from larger spritesheet
        image = pg.Surface((width,height))
        image.blit(self.spritesheet,(0,0),(x,y,width,height)) #can take area as argument too.  pygame.surface.blit()
        image = pg.transform.scale(image,(int(width/2),int(height/2)))
        return image






class Player(pg.sprite.Sprite):

    
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.image.set_colorkey(BLACK)
        self.rect= self.image.get_rect()
        self.rect.center= (WIDTH/2,HEIGHT/2)
        self.pos = vec(WIDTH/2,HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        #self.jumpFlag = False


    def load_images(self):
        self.standing_frames = [self.game.spritesheet.get_image(614,1063,120,191),
                                self.game.spritesheet.get_image(690,406,120,201)]
        for frame in self.standing_frames:
            frame.set_colorkey(BLACK)
        self.walk_frames_r = [self.game.spritesheet.get_image(678,860,120,201),self.game.spritesheet.get_image(692,1458,120,207)]
        self.walk_frames_l =[]
        #flip the images to get left effect
        for frames in self.walk_frames_r:
            frames.set_colorkey(BLACK)
            self.walk_frames_l.append(pg.transform.flip(frames,True,False))
        
        self.jump_frame = self.game.spritesheet.get_image(382,763,150,181)
        self.jump_frame.set_colorkey(BLACK)
    def return_top(self):  #actually returns center 
        return self.rect.center[1]

    def jump(self):
        #self.jumpFlag = True
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self,self.game.platforms,False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP
            
    def animate(self):
        now = pg.time.get_ticks()
        if abs(self.vel.x) < 0.1 and abs(self.vel.x) >= 0:
            self.walking = False
        else:
            self.walking = True

        if self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame +1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self.vel.x > 0: #right
                    self.image =self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
        

        if not self.jumping and not self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                self.image = self.standing_frames[self.current_frame]

        
    def update(self):
        self.animate()
        self.acc = vec(0,PLAYER_GRAV)  
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        #Friction
        self.acc.x += self.vel.x*PLAYER_FRICTION
        #Newtonian equation calculation
        self.vel += self.acc
        self.pos += self.vel + 0.5* self.acc

        #wrapping around
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        self.rect.midbottom = self.pos  #center is also possible


class Platform(pg.sprite.Sprite):
    
    def __init__(self,game,x,y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        images = [self.game.spritesheet.get_image(0,288,380,94),
                  self.game.spritesheet.get_image(213,1662,201,100)]
        self.image = choice(images) 
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def return_top(self):
        return self.rect.midtop[1]


