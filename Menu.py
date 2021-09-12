import pygame, sys  
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

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state =='piano_mode':
            self.piano_mode()
        if self.state == 'guitar_mode':
            self.guitar_mode()
        if self.state == 'autoplay_mode':
            self.autoplay_mode()

game_state = GameState()
while True:
    game_state.state_manager()
    pygame.display.update()
