import pygame, sys  
import time
pygame.init()

# Game Screen
#1250, 700
#800. 437

res = (800,437)
screen = pygame.display.set_mode(res)


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
dark_red = (139, 20, 20)
light_green = (97, 168, 74)
dark_green = (50, 117, 29)

#Actual music
keyboardLong = pygame.image.load('Lettered Keyboard Long.png')
instrumentSound = ''
#playType =''
 
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
guitarSounds = [pygame.mixer.Sound('IndividualSounds/Piano/3_piano_c.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/3_acoustic_d.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/3_acoustic_e.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/3_acoustic_f.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/3_acoustic_g.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/3_acoustic_a.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/3_acoustic_b.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_c.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_d.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_e.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_f.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_g.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_a.wav'), pygame.mixer.Sound('IndividualSounds/AcousticGuitar/4_acoustic_b.wav'),
pygame.mixer.Sound('IndividualSounds/AcousticGuitar/5_acoustic_c.wav')]
#IndividualSounds/AcousticGuitar/3_acoustic_c.wav

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

'''
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


'''
############################################################################################################################################

pianoImage = pygame.image.load("piano.png")
guitarImage = pygame.image.load("guitar.png")

#Button Info
rectHeight = 100
rectWidth = 300
smallWidth = 225
rectDimensions = (rectHeight, rectWidth)
leftButtonX = 40
middleButtonX = 285
rightButtonX = 530
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
            #If user clicks top- taken to piano
            #bottom- taken to guitar
                if oneButtonX <= mouse[0] <= oneButtonX + rectWidth and topButtonY <= mouse[1] <= topButtonY+rectHeight:
                    self.state = 'piano_mode'
                elif twoButtonX <= mouse[0] <= twoButtonX + rectWidth and topButtonY <= mouse[1] <= topButtonY+rectHeight:
                    self.state = 'guitar_mode'
                elif twoButtonX <= mouse[0] <= twoButtonX + rectWidth and botButtonY <= mouse[1] <= botButtonY+rectHeight:
                    self.state = 'autoplay_mode'
                elif oneButtonX <= mouse[0] <= oneButtonX + rectWidth and botButtonY <= mouse[1] <= botButtonY+rectHeight:
                    self.state = 'freeplay_mode'
        screen.fill((beige))       
        pygame.draw.rect(screen,brown,[oneButtonX,topButtonY,rectWidth,rectHeight]) #piano
        pygame.draw.rect(screen,brown,[twoButtonX,topButtonY,rectWidth,rectHeight]) #guitar
        pygame.draw.rect(screen,brown,[oneButtonX,botButtonY,rectWidth,rectHeight]) #freeplay
        pygame.draw.rect(screen,brown,[twoButtonX,botButtonY,rectWidth,rectHeight]) #autoplay
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

    def piano_mode(self):
        instrumentSound = 'piano'
        mouse = pygame.mouse.get_pos() 
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:             
                if oneButtonX <= mouse[0] <= oneButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
                    pygame.quit()
                elif twoButtonX <= mouse[0] <= twoButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
                    pygame.quit()
                elif 5 <= mouse[0] <= 5+80 and 10 <= mouse[1] <= 10+40:
                    self.state = 'intro'   
        screen.fill((light_blue))
        screen.blit(pianoImage,(15,-100))

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

    def guitar_mode(self):
        instrumentSound = 'guitar'
        mouse = pygame.mouse.get_pos() 
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:             
            #if the mouse is clicked on the
            # button the game is terminated
            #10 is x val  100 is y val
                if oneButtonX <= mouse[0] <= oneButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
                    pygame.quit()
                elif twoButtonX <= mouse[0] <= twoButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
                    pygame.quit()
                elif 5 <= mouse[0] <= 5+80 and 10 <= mouse[1] <= 10+40:
                    self.state = 'intro'   
        screen.fill((light_green))
        screen.blit(guitarImage,(150,5))

        pygame.draw.rect(screen,dark_green, [oneButtonX,midButtonY,rectWidth,rectHeight])
        pygame.draw.rect(screen,dark_green, [twoButtonX,midButtonY,rectWidth,rectHeight])
        pygame.draw.rect(screen,dark_green, [5, 10, 60, 25])
        if oneButtonX <= mouse[0] <= oneButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
            pygame.draw.rect(screen,dark_gray, [oneButtonX,midButtonY,rectWidth,rectHeight])     
        elif twoButtonX <= mouse[0] <= twoButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:  
            pygame.draw.rect(screen,dark_gray, [twoButtonX,midButtonY,rectWidth,rectHeight])
        elif  5 <= mouse[0] <= 5+80 and 10 <= mouse[1] <= 10+40:
            pygame.draw.rect(screen,dark_gray, [5, 10, 60,25])
      
        screen.blit(easyButton, (oneButtonX + 80, midButtonY + 22))
        screen.blit(hardButton, (twoButtonX + 80, midButtonY + 22))
        screen.blit(backButton, (10,13))

    def freeplay_mode(self):
        mouse = pygame.mouse.get_pos() 
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:             
                if oneButtonX <= mouse[0] <= oneButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
                    instrumentSound = 'piano'
                    self.state = 'sound'
                elif twoButtonX <= mouse[0] <= twoButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
                    instrumentSound = 'guitar'
                    self.state = 'sound'
                elif 5 <= mouse[0] <= 5+80 and 10 <= mouse[1] <= 10+40:
                    self.state = 'intro'   
        screen.fill((light_gray))


        pygame.draw.rect(screen,dark_green, [oneButtonX,midButtonY,rectWidth,rectHeight])
        pygame.draw.rect(screen,dark_green, [twoButtonX,midButtonY,rectWidth,rectHeight])
        pygame.draw.rect(screen,dark_green, [5, 10, 60, 25])
        if oneButtonX <= mouse[0] <= oneButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
            pygame.draw.rect(screen,dark_gray, [oneButtonX,midButtonY,rectWidth,rectHeight])     
        elif twoButtonX <= mouse[0] <= twoButtonX+rectWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:  
            pygame.draw.rect(screen,dark_gray, [twoButtonX,midButtonY,rectWidth,rectHeight])
        elif  5 <= mouse[0] <= 5+80 and 10 <= mouse[1] <= 10+40:
            pygame.draw.rect(screen,dark_gray, [5, 10, 60,25])
      
        screen.blit(pianoButton, (oneButtonX + 80, midButtonY + 22))
        screen.blit(guitarButton, (twoButtonX + 80, midButtonY + 22))
        screen.blit(backButton, (10,13))


    def autoplay_mode(self):
        mouse = pygame.mouse.get_pos() 
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:             
            #if the mouse is clicked on the
            # button the game is terminated
            #10 is x val  100 is y val
                if oneButtonX <= mouse[0] <= oneButtonX+smallWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
                    pygame.quit()
                elif twoButtonX <= mouse[0] <= twoButtonX+smallWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
                    pygame.quit()
                elif 5 <= mouse[0] <= 5+80 and 10 <= mouse[1] <= 10+40:
                    self.state = 'intro'   
        screen.fill((light_red))
        pygame.draw.rect(screen,dark_red, [leftButtonX,midButtonY,smallWidth,rectHeight])
        pygame.draw.rect(screen,dark_red, [middleButtonX,midButtonY,smallWidth,rectHeight])
        pygame.draw.rect(screen,dark_red, [rightButtonX,midButtonY,smallWidth,rectHeight])
        pygame.draw.rect(screen,dark_red, [5, 10, 60, 25])
        if leftButtonX <= mouse[0] <= leftButtonX+smallWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:
            pygame.draw.rect(screen,dark_gray, [leftButtonX,midButtonY,smallWidth,rectHeight])     
        elif middleButtonX <= mouse[0] <= middleButtonX+smallWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight:  
            pygame.draw.rect(screen,dark_gray, [middleButtonX,midButtonY,smallWidth,rectHeight])
        elif rightButtonX <= mouse[0] <= rightButtonX+smallWidth and midButtonY <= mouse[1] <= midButtonY+rectHeight: 
            pygame.draw.rect(screen,dark_gray, [rightButtonX,midButtonY,smallWidth,rectHeight])
        elif  5 <= mouse[0] <= 5+80 and 10 <= mouse[1] <= 10+40:
            pygame.draw.rect(screen,dark_gray, [5, 10, 60,25])
      
        screen.blit(easyButton, (leftButtonX + 40, midButtonY + 22))
        screen.blit(hardButton, (middleButtonX + 40, midButtonY + 22))
        screen.blit(hardButton, (rightButtonX + 40, midButtonY + 22))
        screen.blit(backButton, (10,13))

    def sound(self):
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                pygame.quit()
        res = (1250,700)
        screen = pygame.display.set_mode(res)
        screen.fill(light_gray)
        screen.blit(keyboardLong, (141,220))

        pianoSounds = [pygame.mixer.Sound('IndividualSounds/Piano/3_piano_c.wav'), pygame.mixer.Sound('IndividualSounds/Piano/3_piano_d.wav'),
                pygame.mixer.Sound('IndividualSounds/Piano/3_piano_e.wav'), pygame.mixer.Sound('IndividualSounds/Piano/3_piano_f.wav'),
                pygame.mixer.Sound('IndividualSounds/Piano/3_piano_g.wav'), pygame.mixer.Sound('IndividualSounds/Piano/3_piano_a.wav'),
                pygame.mixer.Sound('IndividualSounds/Piano/3_piano_b.wav'), pygame.mixer.Sound('IndividualSounds/Piano/4_piano_c.wav'),
                pygame.mixer.Sound('IndividualSounds/Piano/4_piano_d.wav'), pygame.mixer.Sound('IndividualSounds/Piano/4_piano_e.wav'),
                pygame.mixer.Sound('IndividualSounds/Piano/4_piano_f.wav'), pygame.mixer.Sound('IndividualSounds/Piano/4_piano_g.wav'),
                pygame.mixer.Sound('IndividualSounds/Piano/4_piano_a.wav'), pygame.mixer.Sound('IndividualSounds/Piano/4_piano_b.wav'),
                pygame.mixer.Sound('IndividualSounds/Piano/5_piano_c.wav')]

        instrument = instrumentSound
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if (instrument is 'piano'):
                pianoSounds[0].play()
            elif (instrument is 'guitar'):
                guitarSounds[0].play()
            elif (instrument is 'electric'):
                electricSounds[0].play()
        if keys[pygame.K_s]:
            if (instrument is 'piano'):
                pianoSounds[1].play()
            elif (instrument is 'guitar'):
                guitarSounds[1].play()
            elif (instrument is 'electric'):
                electricSounds[1].play()
        if keys[pygame.K_d]:
            if (instrument is 'piano'):
                pianoSounds[2].play()
            elif (instrument is 'guitar'):
                guitarSounds[2].play()
            elif (instrument is 'electric'):
                electricSounds[2].play()
        if keys[pygame.K_f]:
            if (instrument is 'piano'):
                pianoSounds[3].play()
            elif (instrument is 'guitar'):
                guitarSounds[3].play()
            elif (instrument is 'electric'):
                electricSounds[3].play()
        if keys[pygame.K_g]:
            if (instrument is 'piano'):
                pianoSounds[4].play()
            elif (instrument is 'guitar'):
                guitarSounds[4].play()
            elif (instrument is 'electric'):
                electricSounds[4].play()
        if keys[pygame.K_h]:
            if (instrument is 'piano'):
                pianoSounds[5].play()
            elif (instrument is 'guitar'):
                guitarSounds[5].play()
            elif (instrument is 'electric'):
                electricSounds[5].play()
        if keys[pygame.K_j]:
            if (instrument is 'piano'):
                pianoSounds[6].play()
            elif (instrument is 'guitar'):
                guitarSounds[6].play()
            elif (instrument is 'electric'):
                electricSounds[6].play()
        if keys[pygame.K_q]:
            if (instrument is 'piano'):
                pianoSounds[7].play()
            elif (instrument is 'guitar'):
                guitarSounds[7].play()
            elif (instrument is 'electric'):
                electricSounds[7].play()
        if keys[pygame.K_w]:
            if (instrument is 'piano'):
                pianoSounds[8].play()
            elif (instrument is 'guitar'):
                guitarSounds[8].play()
            elif (instrument is 'electric'):
                electricSounds[8].play()
        if keys[pygame.K_e]:
            if (instrument is 'piano'):
                pianoSounds[9].play()
            elif (instrument is 'guitar'):
                guitarSounds[9].play()
            elif (instrument is 'electric'):
                electricSounds[9].play()
        if keys[pygame.K_r]:
            if (instrument is 'piano'):
                pianoSounds[10].play()
            elif (instrument is 'guitar'):
                guitarSounds[10].play()
            elif (instrument is 'electric'):
                electricSounds[10].play()
        if keys[pygame.K_t]:
            if (instrument is 'piano'):
                pianoSounds[11].play()
            elif (instrument is 'guitar'):
                guitarSounds[11].play()
            elif (instrument is 'electric'):
                electricSounds[11].play()
        if keys[pygame.K_y]:
            if (instrument is 'piano'):
                pianoSounds[12].play()
            elif (instrument is 'guitar'):
                guitarSounds[12].play()
            elif (instrument is 'electric'):
                electricSounds[12].play()
        if keys[pygame.K_u]:
            if (instrument is 'piano'):
                pianoSounds[13].play()
            elif (instrument is 'guitar'):
                guitarSounds[13].play()
            elif (instrument is 'electric'):
                electricSounds[13].play()
        if keys[pygame.K_i]:
            if (instrument is 'piano'):
                pianoSounds[14].play()
            elif (instrument is 'guitar'):
                guitarSounds[14].play()
            elif (instrument is 'electric'):
                electricSounds[14].play()

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state =='piano_mode':
            self.piano_mode()
        if self.state == 'guitar_mode':
            self.guitar_mode()
        if self.state == 'autoplay_mode':
            self.autoplay_mode()
        if self.state == 'freeplay_mode':
            self.freeplay_mode()
        if self.state == 'sound':
            self.sound()

game_state = GameState()
while True:
    game_state.state_manager()
    pygame.display.update()
