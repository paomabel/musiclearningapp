#from playsound import playsound

import pygame
from pygame.constants import USEREVENT
import random
pygame.init()

win = pygame.display.set_mode((800,437))
pygame.display.set_caption("First Game")

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isjump = False
        self.jcount = 10
        self.left = False
        self.right = False
        self.walknum = 0
        self.falling = False
    def draw(self,win):
        
        if self.walknum+1 >= 30:
            self.walknum = 0
            self.hitbox = (self.x+ 4,self.y,self.width-120,self.height+20)
        if self.right:
            win.blit(walkright,(self.x,self.y))
            self.walknum += 1
            self.hitbox = (self.x+ 4,self.y,self.width-120,self.height+20)
        elif self.left:
            win.blit(walkleft,(self.x,self.y))
            self.walknum+=1
            self.hitbox = (self.x+ 4,self.y,self.width-120,self.height+20)
        elif self.falling:
            win.blit(fall, (self.x,self.y+30))
            self.hitbox = (self.x+ 4,self.y,self.width-120,self.height+20)
        else:
            win.blit(charact,(self.x,self.y))
            self.hitbox = (self.x+ 4,self.y,self.width-120,self.height+20)
        pygame.draw.rect(win,(100,100,100), self.hitbox,2)
'''x = 50
y = 550
width = 200
height = 100
vel = 10

left = False
right = False
isjump = False
jcount = 10
walknum = 0'''
run = True
clock = pygame.time.Clock()

walkright = pygame.image.load('gamepictures/csright.png')#,pygame.image.load('gamepictures/cs2right.png')]
walkleft = pygame.image.load('gamepictures/csleft.png')#,pygame.image.load('gamepictures/charactersprite2left.png')]
bg = pygame.image.load('gamepictures/bg2.jpg')
charact = pygame.image.load('gamepictures/csright.png') #,pygame.image.load('gamepictures/cs2right.png')]
fall = pygame.image.load('gamepictures/csfall.png')
bgX = 0 
bgx2 = bg.get_width()
class obstacle12(object):
    obs = pygame.image.load('gamepictures/rock.png')
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x,y,width,height)
        self.count = 0
    def draw(self,win):
        self.hitbox = (self.x + 5, self.y + 5,self.width - 10,self.height )
        if self.count >= 8:
            self.count = 0
        win.blit(self.obs, (self.x,self.y))
        self.count+=1
        pygame.draw.rect(win,(100,100,100),self.hitbox,2)
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] + self.hitbox[2]:
          if rect[1] + rect[3] > self.hitbox[1]:
              return True
        return False   
def redrawGamewindow():
    global walknum
    win.blit(bg, (bgX,0))
    win.blit(bg, (bgx2,0))
    jimmy.draw(win)
    #evilnotes.draw(win)
    for r in object1:
        r.draw(win)
    #pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()

pygame.time.set_timer(USEREVENT+1,500)
pygame.time.set_timer(USEREVENT+2,random.randrange(500,4000))
speed = 30
#evilnotes = obstacle12(300,320,90,50)
jimmy = player(50,260,200,100) #jimmy for jimmy hendrix

object1 = []

while run:

    pygame.time.delay(70)

    for z in object1:
        if z.collide(jimmy.hitbox):
            jimmy.falling = True
            #pygame.time.delay(250)
        z.x -= 1.4
        if z.x < - z.width * .1:
            object1.pop(object1.index(z))
    
    bgX -= 3
    bgx2 -= 3
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX < bg.get_width() * -1:
        bgx2 = bg.get_width()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == USEREVENT+1:
            speed += 30
        if event.type == USEREVENT+2:
            r = random.randrange(0,2)
            if r == 0:
                object1.append(obstacle12(300,320,90,50))
    clock.tick(speed)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and jimmy.x > jimmy.vel:
        jimmy.x -= jimmy.vel
        jimmy.left = True
        jimmy.right = False
    elif keys[pygame.K_RIGHT] and jimmy.x < 1400 - jimmy.width - jimmy.vel:
        jimmy.x += jimmy.vel
        jimmy.right = True
        jimmy.left = False
    else:
        jimmy.right = False
        jimmy.left = False
        jwalknum = 0
    if not(jimmy.isjump):
        if keys[pygame.K_SPACE]:
            jimmy.isjump = True
            jimmy.right = False
            jimmy.left = False
            jimmy.walknum = 0
    else:
        if jimmy.jcount >= -10:
            neg = 1
            if jimmy.jcount < 0:
                neg = -1
            jimmy.y -= (jimmy.jcount **2) * 0.5 *neg
            jimmy.jcount -= 1
        else:
            jimmy.isjump = False
            jimmy.jcount = 10
    redrawGamewindow()
pygame.quit()
#playsound('import.mp3')