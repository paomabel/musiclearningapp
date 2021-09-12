import pygame, sys, time
pygame.init()

# Game Screen
#1250, 700
#800. 437

keyboardLong = pygame.image.load('Lettered Keyboard Long.png')

res = (800,437)
screen = pygame.display.set_mode(res)


x_pos = 141
y_pos = 390
#width = 1250 #800
#height = 700 #437
#win = pygame.display.set_mode((width,height))
#win.fill((199,187,143))
#pygame.display.set_caption("Free Play")


instrumentSound = ''
playType =''

#Declaring colors
white = (255,255,255)
beige = (199, 187, 143)
brown = (117, 78, 29)
light_blue = (117, 170, 255)
dark_blue = (36, 99, 201)
black = (0,0,0)
light_gray = (170,170,170)
dark_gray = (100,100,100)
light_red = (191, 71, 71)
dark_red = (158, 35, 35)

gui_font = pygame.font.Font(None,30)

#Button Info
rectHeight = 100
rectWidth = 300
rectDimensions = (rectHeight, rectWidth)
#leftButtonX = 75
#middleButtonX = 475
#rightButtonX = 875
oneButtonX = 75
twoButtonX = 425
topButtonY = 75
midButtonY = 150
botButtonY = 225


buttonFont = pygame.font.SysFont('Corbel',55, bold = True)
backButtonFont = pygame.font.SysFont('Corbel',20, bold = True)
pianoButton = buttonFont.render('PIANO' , True , white)
guitarButton = buttonFont.render('GUITAR', True, white)
freeButton = buttonFont.render('FREE PLAY', True, white)
autoButton = buttonFont.render('AUTO PLAY', True, white)
easyButton = buttonFont.render('EASY', True, white)
hardButton = buttonFont.render('HARD', True, white)
backButton = backButtonFont.render('BACK', True, white)

########################################################################################################################################

#musical components
notes = ['c3', 'd3', 'e3', 'f3', 'g3', 'a3', 'b3', 'c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4', 'c5']

#songs
happy_bday = ['g3', 'g3', 'a3', 'rest', 'g3', 'rest', 'c4', 'rest', 'b3', 'rest', 'rest', 'rest', 
'g3', 'g3', 'a3', 'rest', 'g3', 'rest', 'd4', 'rest', 'c4', 'rest', 'rest', 'rest', 'g3', 'g3', 'g4',
'rest', 'e4', 'rest', 'c4', 'c4', 'b3', 'rest', 'a3','rest', 'f4', 'f4', 'e4', 'rest', 'c4', 'rest', 'd4','rest', 'c4']

twinkle = ['g3', 'rest', 'g3', 'rest', 'd4', 'rest', 'd4', 'rest', 'e4','rest', 'e4', 'rest', 'd4', 'rest', 'rest', 'rest',
'c4', 'rest', 'c4', 'rest', 'b3', 'rest', 'b3', 'rest', 'a3', 'rest', 'a3', 'rest', 'g3', 'rest', 'rest', 'rest', 'd4', 'rest', 'd4',
'rest', 'c4', 'rest', 'c4', 'rest', 'b3', 'rest', 'b3', 'rest', 'a3', 'rest', 'rest', 'rest', 'd4', 'rest', 'd4',
'rest', 'c4', 'rest', 'c4', 'rest', 'b3', 'rest', 'b3', 'rest', 'a3', 'rest', 'rest', 'rest', 'g3', 'rest', 'g3', 'rest',
'd4', 'rest', 'd4', 'rest', 'e4', 'rest', 'e4', 'rest', 'd4', 'rest', 'rest', 'rest', 'c4', 'rest', 'c4', 'rest', 'b3',
'rest', 'b3', 'rest', 'a3', 'rest', 'a3', 'rest', 'g3', 'rest', 'rest', 'rest']

heart_and_soul = ['rest', 'c4', 'rest', 'c4', 'e4', 'rest', 'rest', 'e4', 'a3', 'rest', 'rest', 'a3', 'c4','rest', 'rest', 'c4', 'd4',
'rest', 'rest', 'd4', 'f4', 'rest', 'rest', 'f4', 'g3', 'rest', 'rest', 'g3', 'b3', 'rest', 'b3', 'c4', 'rest', 'rest', 
'c4', 'rest', 'rest', 'c4', 'rest', 'rest', 'rest', 'rest', 'rest', 'rest', 'rest', 'rest', 'c4', 'b3',
'rest', 'a3', 'b3', 'rest', 'c4', 'd4', 'rest', 'e4', 'rest', 'rest', 'e4', 'rest', 'rest','e4', 'rest', 'rest',
'rest', 'rest', 'rest', 'rest', 'rest', 'rest', 'e4', 'd4', 'rest', 'c4', 'd4', 'rest', 'e4', 'f4', 'rest', 'g4',
'rest', 'rest', 'rest', 'rest', 'rest', 'c4', 'rest', 'rest', 'rest', 'rest', 'rest', 'rest', 'rest', 'a4', 'g4', 'f4', 'e4', 'rest',
'd4', 'rest', 'c4', 'rest', 'rest', 'c5', 'rest', 'b4', 'a4', 'rest', 'rest', 'a4', 'rest', 'g4', 'f4', 'rest', 'rest', 'f4', 'rest',
'e4', 'd4', 'c4', 'rest', 'rest', 'c4', 'rest', 'rest']

#Acoustic guitar sounds
guitarSounds = [pygame.mixer.Sound('IndividualSounds/AcousticGuitar/3_acoustic_c.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/3_acoustic_d.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/3_acoustic_e.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/3_acoustic_f.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/3_acoustic_g.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/3_acoustic_a.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/3_acoustic_b.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_c.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_d.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_e.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_f.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_g.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_a.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_b.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/5_acoustic_c.wav')]

#Piano sounds
pianoSounds = [pygame.mixer.Sound('IndividualSounds/Piano/3_piano_c.wav'), pygame.mixer.Sound('IndividualSounds/Piano/3_piano_d.wav'),
pygame.mixer.Sound('IndividualSounds/Piano/3_piano_e.wav'), pygame.mixer.Sound('IndividualSounds/Piano/3_piano_f.wav'),
pygame.mixer.Sound('IndividualSounds/Piano/3_piano_g.wav'), pygame.mixer.Sound('IndividualSounds/Piano/3_piano_a.wav'),
pygame.mixer.Sound('IndividualSounds/Piano/3_piano_b.wav'), pygame.mixer.Sound('IndividualSounds/Piano/4_piano_c.wav'),
pygame.mixer.Sound('IndividualSounds/Piano/4_piano_d.wav'), pygame.mixer.Sound('IndividualSounds/Piano/4_piano_e.wav'),
pygame.mixer.Sound('IndividualSounds/Piano/4_piano_f.wav'), pygame.mixer.Sound('IndividualSounds/Piano/4_piano_g.wav'),
pygame.mixer.Sound('IndividualSounds/Piano/4_piano_a.wav'), pygame.mixer.Sound('IndividualSounds/Piano/4_piano_b.wav'),
pygame.mixer.Sound('IndividualSounds/Piano/5_piano_c.wav')]

#Electric Guitar sounds
electricSounds = [pygame.mixer.Sound('IndividualSounds/ElectricGuitar/2_electric_c.wav'), pygame.mixer.Sound('IndividualSounds/ElectricGuitar/2_electric_d.wav'),
pygame.mixer.Sound('IndividualSounds/ElectricGuitar/2_electric_e.wav'), pygame.mixer.Sound('IndividualSounds/ElectricGuitar/2_electric_f.wav'),
pygame.mixer.Sound('IndividualSounds/ElectricGuitar/2_electric_g.wav'), pygame.mixer.Sound('IndividualSounds/ElectricGuitar/2_electric_a.wav'),
pygame.mixer.Sound('IndividualSounds/ElectricGuitar/2_electric_b.wav'), pygame.mixer.Sound('IndividualSounds/ElectricGuitar/3_electric_c.wav'),
pygame.mixer.Sound('IndividualSounds/ElectricGuitar/3_electric_d.wav'), pygame.mixer.Sound('IndividualSounds/ElectricGuitar/3_electric_e.wav'),
pygame.mixer.Sound('IndividualSounds/ElectricGuitar/3_electric_f.wav'), pygame.mixer.Sound('IndividualSounds/ElectricGuitar/3_electric_g.wav'),
pygame.mixer.Sound('IndividualSounds/ElectricGuitar/3_electric_a.wav'), pygame.mixer.Sound('IndividualSounds/ElectricGuitar/3_electric_b.wav'),
pygame.mixer.Sound('IndividualSounds/ElectricGuitar/4_electric_c.wav')]

#Xylophone sounds
xyloSounds = [pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_c.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_d.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_e.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_f.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_g.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_a.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_b.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_c.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_d.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_e.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_f.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_g.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_a.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_b.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/8_xylo_c.wav')]

############################################################################################################################################

def redrawGamewindow():
    if True:
        screen.blit(keyboardLong, (141,220))
    pygame.display.update()

def highlightKey():
    if True:
        pygame.draw.rect(screen, (0, 0, 255), (x_pos, y_pos, 64, 86))
    pygame.display.update()

def autoplaySong(song, instrument):
    for i in song:
        if (i is 'c3'):
            if (instrument is 'piano'):
                pianoSounds[0].play()
            elif (instrument is 'guitar'):
                guitarSounds[0].play()
            time.sleep(0.5)
        elif (i is 'd3'):
            if (instrument is 'piano'):
                pianoSounds[1].play()
            elif (instrument is 'guitar'):
                guitarSounds[1].play()
            time.sleep(0.5)
        elif (i is 'e3'):
            if (instrument is 'piano'):
                pianoSounds[2].play()
            elif (instrument is 'guitar'):
                guitarSounds[2].play()
            time.sleep(0.5)
        elif (i is 'f3'):
            if (instrument is 'piano'):
                pianoSounds[3].play()
            elif (instrument is 'guitar'):
                guitarSounds[3].play()
            time.sleep(0.5)
        elif (i is 'g3'):
            if (instrument is 'piano'):
                pianoSounds[4].play()
            elif (instrument is 'guitar'):
                guitarSounds[4].play()
            time.sleep(0.5)
        elif (i is 'a3'):
            if (instrument is 'piano'):
                pianoSounds[5].play()
            elif (instrument is 'guitar'):
                guitarSounds[5].play()
            time.sleep(0.5)
        elif (i is 'b3'):
            if (instrument is 'piano'):
                pianoSounds[6].play()
            elif (instrument is 'guitar'):
                guitarSounds[6].play()
            time.sleep(0.5)
        elif (i is 'c4'):
            if (instrument is 'piano'):
                pianoSounds[7].play()
            elif (instrument is 'guitar'):
                guitarSounds[7].play()
            time.sleep(0.5)
        elif (i is 'd4'):
            if (instrument is 'piano'):
                pianoSounds[8].play()
            elif (instrument is 'guitar'):
                guitarSounds[8].play()
            time.sleep(0.5)
        elif (i is 'e4'):
            if (instrument is 'piano'):
                pianoSounds[9].play()
            elif (instrument is 'guitar'):
                guitarSounds[9].play()
            time.sleep(0.5)
        elif (i is 'f4'):
            if (instrument is 'piano'):
                pianoSounds[10].play()
            elif (instrument is 'guitar'):
                guitarSounds[10].play()
            time.sleep(0.5)
        elif (i is 'g4'):
            if (instrument is 'piano'):
                pianoSounds[11].play()
            elif (instrument is 'guitar'):
                guitarSounds[11].play()
            time.sleep(0.5)
        elif (i is 'a4'):
            if (instrument is 'piano'):
                pianoSounds[12].play()
            elif (instrument is 'guitar'):
                guitarSounds[12].play()
            time.sleep(0.5)
        elif (i is 'b4'):
            if (instrument is 'piano'):
                pianoSounds[13].play()
            elif (instrument is 'guitar'):
                guitarSounds[13].play()
            time.sleep(0.5)
        elif (i is 'c5'):
            if (instrument is 'piano'):
                pianoSounds[14].play()
            elif (instrument is 'guitar'):
                guitarSounds[14].play()
            time.sleep(0.5)
        else:
            time.sleep(0.5)
    redrawGamewindow()

class GameState():
    def __init__(self):
        self.state = 'intro'

    def buttons(screen, color, rectX, rectY, rectWidth, rectHeight):
        pygame.draw.rect(screen, color, [rectX ,rectY ,rectWidth, rectHeight])
        
    def intro(self):
        mouse = pygame.mouse.get_pos() 
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:             
            #if the mouse is clicked on the
            # button the game is terminated

                #Piano Button
                if oneButtonX <= mouse[0] <= oneButtonX + rectWidth and topButtonY <= mouse[1] <= topButtonY+rectHeight:
                    self.state = 'main_game'
                    instrumentSound = 'piano'
                #Guitar Button
                elif twoButtonX <= mouse[0] <= twoButtonX + rectWidth and topButtonY <= mouse[1] <= topButtonY+rectHeight:
                    self.state = 'main_game'
                    instrumentSound = 'guitar'
        screen.fill((beige))   
      
        pygame.draw.rect(screen,brown,[oneButtonX,topButtonY,rectWidth,rectHeight])
        pygame.draw.rect(screen,brown,[twoButtonX,topButtonY,rectWidth,rectHeight])
        pygame.draw.rect(screen,brown,[oneButtonX,botButtonY,rectWidth,rectHeight]) 
        pygame.draw.rect(screen,brown,[twoButtonX,botButtonY,rectWidth,rectHeight]) 
        if oneButtonX <= mouse[0] <= oneButtonX+rectWidth and topButtonY <= mouse[1] <= topButtonY+rectHeight:
            pygame.draw.rect(screen,dark_gray,[oneButtonX,topButtonY,rectWidth,rectHeight])        
        elif twoButtonX <= mouse[0] <= twoButtonX+rectWidth and topButtonY <= mouse[1] <= topButtonY+rectHeight:   
            pygame.draw.rect(screen,dark_gray,[twoButtonX,topButtonY,rectWidth,rectHeight]) 
        elif oneButtonX <= mouse[0] <= oneButtonX+rectWidth and botButtonY <= mouse[1] <= botButtonY+rectHeight:   
            pygame.draw.rect(screen,dark_gray,[oneButtonX,botButtonY,rectWidth,rectHeight]) 
        elif twoButtonX <= mouse[0] <= twoButtonX+rectWidth and botButtonY <= mouse[1] <= botButtonY+rectHeight:   
            pygame.draw.rect(screen,dark_gray,[twoButtonX,botButtonY,rectWidth,rectHeight]) 
        screen.blit(pianoButton, (oneButtonX + 65, topButtonY + 22))
        screen.blit(guitarButton, (twoButtonX + 55, topButtonY + 22))
        screen.blit(freeButton, (oneButtonX + 15, botButtonY + 22))
        screen.blit(autoButton, (twoButtonX + 8, botButtonY + 22))

    def main_game(self):
        mouse = pygame.mouse.get_pos() 
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:             
            #if the mouse is clicked on the
            # button the game is terminated
            #10 is x val  100 is y val

                #Free Play
                if oneButtonX <= mouse[0] <= oneButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
                    pygame.quit()
                    self.state = 'free'
                #Autoplay
                elif twoButtonX <= mouse[0] <= twoButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
                    pygame.quit()
                    self.state = 'auto'
                #Back button
                elif 5 <= mouse[0] <= 5+80 and 10 <= mouse[1] <= 10+40:
                    self.state = 'intro'   
        screen.fill((light_blue))
        pygame.draw.rect(screen,dark_blue, [oneButtonX,midButtonY,rectWidth,rectHeight])
        pygame.draw.rect(screen,dark_blue, [twoButtonX,midButtonY,rectWidth,rectHeight])
        pygame.draw.rect(screen,dark_blue, [5, 10, 60, 25])
        if oneButtonX <= mouse[0] <= oneButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
            pygame.draw.rect(screen,dark_gray, [oneButtonX,midButtonY,rectWidth,rectHeight])     
        elif twoButtonX <= mouse[0] <= twoButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:  
            pygame.draw.rect(screen,dark_gray, [twoButtonX,midButtonY,rectWidth,rectHeight])
        elif  5 <= mouse[0] <= 5+80 and 10 <= mouse[1] <= 10+40:
            pygame.draw.rect(screen,dark_gray, [5, 10, 60,25])
      
        screen.blit(easyButton, (oneButtonX + 80, midButtonY + 22))
        screen.blit(hardButton, (twoButtonX + 80, midButtonY + 22))
        screen.blit(backButton, (10,13))

    '''
    def freePlay(self, instrument):
        width = 1250 #800
        height = 700 #437
        instrument = instrumentSound
        screen = pygame.display.set_mode((width,height))
        screen.fill((199,187,143))
        pygame.display.set_caption("Free Play")
        pygame.display.flip()
        redrawGamewindow()

        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        x = 141
        while True:
            redrawGamewindow()
            if keys[pygame.K_a]:
                highlightKey()
                if (instrument is 'piano'):
                        pianoSounds[0].play()
                elif (instrument is 'guitar'):
                    guitarSounds[0].play()
                elif (instrument is 'electric'):
                    electricSounds[0].play()
            if keys[pygame.K_s]:
                x += 64
                highlightKey()
                if (instrument is 'piano'):
                    pianoSounds[1].play()
                elif (instrument is 'guitar'):
                    guitarSounds[1].play()
                elif (instrument is 'electric'):
                        electricSounds[1].play()
            if keys[pygame.K_d]:
                x += (64 * 2)
                highlightKey()
                if (instrument is 'piano'):
                   pianoSounds[2].play()
                elif (instrument is 'guitar'):
                    guitarSounds[2].play()
                elif (instrument is 'electric'):
                    electricSounds[2].play()
            if keys[pygame.K_f]:
                x += (64 * 3)
                highlightKey()
                if (instrument is 'piano'):
                    pianoSounds[3].play()
                elif (instrument is 'guitar'):
                    guitarSounds[3].play()
                elif (instrument is 'electric'):
                    electricSounds[3].play()
            if keys[pygame.K_g]:
                x += (64 * 4)
                highlightKey()
                if (instrument is 'piano'):
                    pianoSounds[4].play()
                elif (instrument is 'guitar'):
                    guitarSounds[4].play()
                elif (instrument is 'electric'):
                     electricSounds[4].play()
            if keys[pygame.K_h]:
                x += (64 * 5)
                highlightKey()
                if (instrument is 'piano'):
                    pianoSounds[5].play()
                elif (instrument is 'guitar'):
                    guitarSounds[5].play()
                elif (instrument is 'electric'):
                    electricSounds[5].play()
            if keys[pygame.K_j]:
                x += (64 * 6)
                highlightKey()
                if (instrument is 'piano'):
                    pianoSounds[6].play()
                elif (instrument is 'guitar'):
                    guitarSounds[6].play()
                elif (instrument is 'electric'):
                    electricSounds[6].play()
            if keys[pygame.K_q]:
                x += (64 * 7)
                highlightKey()
                if (instrument is 'piano'):
                    pianoSounds[7].play()
                elif (instrument is 'guitar'):
                    guitarSounds[7].play()
                elif (instrument is 'electric'):
                    electricSounds[7].play()
            if keys[pygame.K_w]:
                x += (64 * 8)
                highlightKey()
                if (instrument is 'piano'):
                    pianoSounds[8].play()
                elif (instrument is 'guitar'):
                    guitarSounds[8].play()
                elif (instrument is 'electric'):
                    electricSounds[8].play()
            if keys[pygame.K_e]:
                x += (64 * 9)
                highlightKey()
                if (instrument is 'piano'):
                    pianoSounds[9].play()
                elif (instrument is 'guitar'):
                    guitarSounds[9].play()
                elif (instrument is 'electric'):
                    electricSounds[9].play()
            if keys[pygame.K_r]:
                x += (64 * 10)
                highlightKey()
                if (instrument is 'piano'):
                    pianoSounds[10].play()
                elif (instrument is 'guitar'):
                    guitarSounds[10].play()
                elif (instrument is 'electric'):
                    electricSounds[10].play()
            if keys[pygame.K_t]:
                x += (64 * 11)
                highlightKey()
                if (instrument is 'piano'):
                    pianoSounds[11].play()
                elif (instrument is 'guitar'):
                    guitarSounds[11].play()
                elif (instrument is 'electric'):
                    electricSounds[11].play()
            if keys[pygame.K_y]:
                x += (64 * 12)
                highlightKey()
                if (instrument is 'piano'):
                    pianoSounds[12].play()
                elif (instrument is 'guitar'):
                    guitarSounds[12].play()
                elif (instrument is 'electric'):
                    electricSounds[12].play()
            if keys[pygame.K_u]:
                x += (64 * 13)
                highlightKey()
                if (instrument is 'piano'):
                    pianoSounds[13].play()
                elif (instrument is 'guitar'):
                    guitarSounds[13].play()
                elif (instrument is 'electric'):
                    electricSounds[13].play()
            if keys[pygame.K_i]:
                x += (64 * 14)
                highlightKey()
                if (instrument is 'piano'):
                    pianoSounds[14].play()
                elif (instrument is 'guitar'):
                    guitarSounds[14].play()
                elif (instrument is 'electric'):
                    electricSounds[14].play()
            time.sleep(0.075)
            x = 141
    '''
        
    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state =='main_game':
            self.main_game()
        if self.state == 'free':
            self.freePlay()

game_state = GameState()
while True:
    game_state.state_manager()
    pygame.display.update()