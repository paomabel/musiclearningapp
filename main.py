#from playsound import playsound
import pygame
pygame.init()

win = pygame.display.set_mode((1250,700))
pygame.display.set_caption("First Game")
x = 50
y = 550
width = 200
height = 100
vel = 5 
run = True
left = False
right = False
isjump = False
jcount = 10
walknum = 0

clock = pygame.time.Clock()

walkright = [pygame.image.load('gamepictures/csright.png')]#,pygame.image.load('gamepictures/cs2right.png')]
walkleft = [pygame.image.load('gamepictures/csleft.png')]#,pygame.image.load('gamepictures/charactersprite2left.png')]
bg = pygame.image.load('gamepictures/bg.png')
charact = pygame.image.load('gamepictures/csright.png') #,pygame.image.load('gamepictures/cs2right.png')]

def redrawGamewindow():
    global walknum
    win.blit(bg, (0,0))
    if walknum+1 >= 32:
        walknum = 0
    if right:
        win.blit(walkright[walknum//3],(x,y))
        walknum += 1
    elif left:
        win.blit(walkleft[walknum//3],(x,y))
        walknum+=1
    else:
        win.blit(charact,(x,y))

    #pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()

while run:

    pygame.time.delay(50)
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walknum = 0
    if not(isjump):
        if keys[pygame.K_SPACE]:
            isjump = True
            right = False
            left = False
            walknum = 0
    else:
        if jcount >= -10:
            neg = 1
            if jcount < 0:
                neg = -1
            y -= (jcount **2) *0.5 *neg
            jcount -= 1
        else:
            isjump = False
            jcount = 10
    redrawGamewindow()
pygame.quit()
#playsound('import.mp3')