#jumpy! platform game



import pygame as pg
import random
from settings import *
from sprites import *
from os import path





class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)

    def release_highScore(self):
        #check for highscore in file
        if(path.exists(HS_FILE)):
            print("file exists")
            F=open(HS_FILE,'r')
            self.highScore=F.read()
            F.close()
        



        
        
    def new(self):
        self.score=0
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self)
        self.platforms = pg.sprite.Group()
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)  #list explosion args and kwargs
            self.platforms.add(p)
            self.all_sprites.add(p)
        self.run()
        

    def run(self):
        #game loop
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        
        
    def update(self):
        #game loop - Update
        self.all_sprites.update()
        #check if player hits platform during falling only or velocity == 0
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:  #this thing keeps on hitting
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        #if player reaches top 1/4 of the screen



#die
        #When player Dies or y-position is greater than height
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y,3)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False
            if self.highScore:
                if int(self.highScore) > self.score:
                    self.score=self.highScore
            else:
                file=open(HS_FILE,'w')
                file.write(str(self.score))
                file.close()    
            self.show_go_screen()




        #print(self.player.rect.top)  returns top part of the rectangle
        if self.player.rect.top <= HEIGHT/4:
            self.player.pos.y += abs(self.player.vel.y) #velocity is negative but we need to make this positive
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
       #if platforms are below the visible screen
                if plat.rect.top > HEIGHT:
                    self.platforms.remove(plat) #removing items from list
                    self.all_sprites.remove(plat)
                    self.score += 10

        #spawn new platforms
        while len(self.platforms) < 6:
            width = random.randrange(50,100)
            p = Platform(random.randrange(0,WIDTH-width),
                        random.randrange(-75,-30),
                        width,20)
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing=False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

            



        #game-loop -events
    def draw(self):
        
        self.screen.fill(BG_COLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score),22,WHITE,WIDTH/2,15)

        #flipping the display
        pg.display.flip()

    def show_start_screen(self):
        self.screen.fill(BG_COLOR)
        self.draw_text("Jumpy",48,WHITE,WIDTH/2,HEIGHT/4)
        self.draw_text("Arrows to move, Space to jump",22,WHITE,WIDTH/2,HEIGHT/2)
        self.draw_text("Press any key to play",22,WHITE,WIDTH/2,HEIGHT*3/4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        self.screen.fill(BG_COLOR)
        self.draw_text("Saucy ",48,WHITE,WIDTH/2,HEIGHT/4)
        self.draw_text(str("HIGH SCORE IS : {}".format(self.score)),22,WHITE,WIDTH/2,HEIGHT/2)
        self.draw_text("Press any key to play again",22,WHITE,WIDTH/2,HEIGHT*3/4)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting=True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting=False
                    self.running=False
                if event.type == pg.KEYUP:
                    waiting = False

            
    def draw_text(self,text,size,color,x,y):
        font = pg.font.Font(self.font_name,size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)


g= Game()
g.show_start_screen()
g.release_highScore()
while g.running:
    g.new()
    


pg.quit()
