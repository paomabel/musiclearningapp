#from playsound import playsound
import pygame, time
pygame.init()

x_pos = 141
y_pos = 390
width = 1250 #800
height = 700 #437
run = True

win = pygame.display.set_mode((width,height))
win.fill((199,187,143))
pygame.display.set_caption("Free Play")

keyboardLong = pygame.image.load('Lettered Keyboard Long.png')
keyboardTall = pygame.image.load('Lettered Keyboard 600 600.png')

def redrawGamewindow():
    if True:
        win.blit(keyboardLong, (141,220))
    pygame.display.update()

#musical components
notes = ['c3', 'd3', 'e3', 'f3', 'g3', 'a3', 'b3', 'c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4', 'c5']

'''
def highlightKey():
    if True:
        for i in range(14):
            if notes[i] == 'c3':
                pygame.draw.rect(win, (100, 100, 100), (x_pos, y_pos, 64, 86))
            elif notes[i] == 'd3':
                pygame.draw.rect(win, (100, 100, 100), (x_pos + 64, y_pos, 64, 86))
            elif notes[i] == 'e3':
                pygame.draw.rect(win, (100, 100, 100), (x_pos, y_pos, 64, 86))
            elif notes[i] == 'f3':
                pygame.draw.rect(win, (100, 100, 100), (x_pos + 64 * 2, y_pos + 64 * 3, 64, 86))
            elif notes[i] == 'g3':
                pygame.draw.rect(win, (100, 100, 100), (x_pos + 64 *4, y_pos, 64, 86))
            elif notes[i] == 'a3':
                pygame.draw.rect(win, (100, 100, 100), (x_pos+ 64 * 5, y_pos , 64, 86))
            elif notes[i] == 'b3':
                pygame.draw.rect(win, (100, 100, 100), (x_pos + 64 * 6, y_pos, 64, 86))
            elif notes[i] == 'c4':
                pygame.draw.rect(win, (100, 100, 100), (x_pos + 64 * 7, y_pos, 64, 86))
            elif notes[i] == 'd4':
                pygame.draw.rect(win, (100, 100, 100), (x_pos, y_pos + 64 * 8, 64, 86))
            elif notes[i] == 'e4':
                pygame.draw.rect(win, (100, 100, 100), (x_pos + 64 * 9, y_pos, 64, 86))
            elif notes[i] == 'f4':
                pygame.draw.rect(win, (100, 100, 100), (x_pos + 64 * 10, y_pos, 64, 86))
            elif notes[i] == 'g4':
                pygame.draw.rect(win, (100, 100, 100), (x_pos+ 64 * 11, y_pos , 64, 86))
            elif notes[i] == 'a4':
                pygame.draw.rect(win, (100, 100, 100), (x_pos  + 64 * 12, y_pos, 64, 86))
            elif notes[i] == 'b4':
                pygame.draw.rect(win, (100, 100, 100), (x_pos + 64 * 13, y_pos, 64, 86))
            elif notes[i] == 'c5':
                pygame.draw.rect(win, (100, 100, 100), (x_pos + 64 * 14, y_pos, 64, 86))
        pygame.display.update()
'''


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

#Bass sounds
bassSounds = [pygame.mixer.Sound('IndividualSounds/Bass/2_bass_c.wav'), pygame.mixer.Sound('IndividualSounds/Bass/2_bass_d.wav'),
pygame.mixer.Sound('IndividualSounds/Bass/2_bass_e.wav'), pygame.mixer.Sound('IndividualSounds/Bass/2_bass_f.wav'),
pygame.mixer.Sound('IndividualSounds/Bass/2_bass_g.wav'), pygame.mixer.Sound('IndividualSounds/Bass/2_bass_a.wav'),
pygame.mixer.Sound('IndividualSounds/Bass/2_bass_b.wav'), pygame.mixer.Sound('IndividualSounds/Bass/3_bass_c.wav'),
pygame.mixer.Sound('IndividualSounds/Bass/3_bass_d.wav'), pygame.mixer.Sound('IndividualSounds/Bass/3_bass_e.wav'),
pygame.mixer.Sound('IndividualSounds/Bass/3_bass_f.wav'), pygame.mixer.Sound('IndividualSounds/Bass/3_bass_g.wav'),
pygame.mixer.Sound('IndividualSounds/Bass/3_bass_a.wav'), pygame.mixer.Sound('IndividualSounds/Bass/3_bass_b.wav'),
pygame.mixer.Sound('IndividualSounds/Bass/4_bass_c.wav')]

#Saxophone sounds
saxSounds = [pygame.mixer.Sound('IndividualSounds/Saxophone/2_sax_c.wav'), pygame.mixer.Sound('IndividualSounds/Saxophone/2_sax_d.wav'),
pygame.mixer.Sound('IndividualSounds/Saxophone/2_sax_e.wav'), pygame.mixer.Sound('IndividualSounds/Saxophone/2_sax_f.wav'),
pygame.mixer.Sound('IndividualSounds/Saxophone/2_sax_g.wav'), pygame.mixer.Sound('IndividualSounds/Saxophone/2_sax_a.wav'),
pygame.mixer.Sound('IndividualSounds/Saxophone/2_sax_b.wav'), pygame.mixer.Sound('IndividualSounds/Saxophone/3_sax_c.wav'),
pygame.mixer.Sound('IndividualSounds/Saxophone/3_sax_d.wav'), pygame.mixer.Sound('IndividualSounds/Saxophone/3_sax_e.wav'),
pygame.mixer.Sound('IndividualSounds/Saxophone/3_sax_f.wav'), pygame.mixer.Sound('IndividualSounds/Saxophone/3_sax_g.wav'),
pygame.mixer.Sound('IndividualSounds/Saxophone/3_sax_a.wav'), pygame.mixer.Sound('IndividualSounds/Saxophone/3_sax_b.wav'),
pygame.mixer.Sound('IndividualSounds/Saxophone/4_sax_c.wav')]

#Xylophone sounds
xyloSounds = [pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_c.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_d.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_e.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_f.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_g.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_a.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/6_xylo_b.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_c.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_d.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_e.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_f.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_g.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_a.wav'), pygame.mixer.Sound('IndividualSounds/Xylophone/7_xylo_b.wav'),
pygame.mixer.Sound('IndividualSounds/Xylophone/8_xylo_c.wav')]

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
            
#############################################################################################################################################################

while run:
    mouse = pygame.mouse.get_pos() 
    pygame.draw.rect(win, (100,100,100), [45, 45, 300, 75])   
    pygame.draw.rect(win, (100,100,100), [400, 45, 350, 75]) 
    pygame.draw.rect(win, (100,100,100), [800, 45, 350, 75])
    buttonFont = pygame.font.SysFont('Corbel',55, bold = True)
    autoButton = buttonFont.render('AUTOPLAY', True, (255,255,255))    
    autoButton_1 = buttonFont.render('AUTOPLAY 2', True, (255,255,255))   
    autoButton_2 = buttonFont.render('AUTOPLAY 3', True, (255,255,255))   
    win.blit(autoButton, (50, 50))
    win.blit(autoButton_1, (400, 50))
    win.blit(autoButton_2, (800, 50))
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #playSong(twinkle, 'guitar')

    instrument = 'guitar'
    keys = pygame.key.get_pressed()


    if event.type == pygame.MOUSEBUTTONDOWN:
        if 45 <= mouse[0] <= 45+300 and 45 <= mouse[1] <= 45+75:
            autoplaySong(twinkle, 'guitar')
        elif 45 <= mouse[0] <= 45+600 and 45 <= mouse[1] <= 45+75:
            autoplaySong(happy_bday, 'piano')
        elif 45 <= mouse[0] <= 45+900 and 45 <= mouse[1] <= 45+75:
            autoplaySong(heart_and_soul, 'guitar')
    if 45 <= mouse[0] <= 45+300 and 45 <= mouse[1] <= 45+75:
        pygame.draw.rect(win,(50,50,50),[45,45,300,75])
    if 300 <= mouse[0] <= 45+600 and 45 <= mouse[1] <= 45+75:
        pygame.draw.rect(win,(50,50,50),[45,45,300,75])
    if 600 <= mouse[0] <= 45+900 and 45 <= mouse[1] <= 45+75:
        pygame.draw.rect(win,(50,50,50),[45,45,300,75])

#   boardLetters = [keys[pygame.K_a], keys[pygame.K_s], keys[pygame.K_d], keys[pygame.K_f], keys[pygame.K_g], keys[pygame.K_h], keys[pygame.K_j], keys[pygame.K_q],
#    keys[pygame.K_w], keys[pygame.K_e], keys[pygame.K_r], keys[pygame.K_t], keys[pygame.K_y], keys[pygame.K_u], keys[pygame.K_i]]

    #playSong(heart_and_soul, 'guitar')
    '''
    i = 0
    if (i <= 14):
        if (boardLetters[i] != True):
            i += 1
        elif boardLetters[i]:
            x += (64 * i)
            highlightKey()
            if (instrument == 'piano'):
                pianoSounds[i].play()
            elif (instrument == 'guitar'):
                guitarSounds[i].play()
            elif (instrument == 'electric'):
                electricSounds[i].play()
            elif (instrument == 'bass'):
                bassSounds[i].play()
            elif (instrument == 'sax'):
                saxSounds[i].play()
    '''
    
    if keys[pygame.K_a]:
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[0].play()
        elif (instrument is 'guitar'):
            guitarSounds[0].play()
        elif (instrument is 'electric'):
            electricSounds[0].play()
        elif (instrument is 'bass'):
            bassSounds[0].play()
        elif (instrument is 'Saxophone'):
            saxSounds[0].play()
    if keys[pygame.K_s]:
        x += 64
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[1].play()
        elif (instrument is 'guitar'):
            guitarSounds[1].play()
        elif (instrument is 'electric'):
            electricSounds[1].play()
        elif (instrument is 'bass'):
            bassSounds[1].play()
        elif (instrument is 'Saxophone'):
            saxSounds[1].play()
    if keys[pygame.K_d]:
        x += (64 * 2)
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[2].play()
        elif (instrument is 'guitar'):
            guitarSounds[2].play()
        elif (instrument is 'electric'):
            electricSounds[2].play()
        elif (instrument is 'bass'):
            bassSounds[2].play()
        elif (instrument is 'Saxophone'):
            saxSounds[2].play()
    if keys[pygame.K_f]:
        x += (64 * 3)
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[3].play()
        elif (instrument is 'guitar'):
            guitarSounds[3].play()
        elif (instrument is 'electric'):
            electricSounds[3].play()
        elif (instrument is 'bass'):
            bassSounds[3].play()
        elif (instrument is 'Saxophone'):
            saxSounds[3].play()
    if keys[pygame.K_g]:
        x += (64 * 4)
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[4].play()
        elif (instrument is 'guitar'):
            guitarSounds[4].play()
        elif (instrument is 'electric'):
            electricSounds[4].play()
        elif (instrument is 'bass'):
            bassSounds[4].play()
        elif (instrument is 'Saxophone'):
            saxSounds[4].play()
    if keys[pygame.K_h]:
        x += (64 * 5)
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[5].play()
        elif (instrument is 'guitar'):
            guitarSounds[5].play()
        elif (instrument is 'electric'):
            electricSounds[5].play()
        elif (instrument is 'bass'):
            bassSounds[5].play()
        elif (instrument is 'Saxophone'):
            saxSounds[5].play()
    if keys[pygame.K_j]:
        x += (64 * 6)
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[6].play()
        elif (instrument is 'guitar'):
            guitarSounds[6].play()
        elif (instrument is 'electric'):
            electricSounds[6].play()
        elif (instrument is 'bass'):
            bassSounds[6].play()
        elif (instrument is 'Saxophone'):
            saxSounds[6].play()
    if keys[pygame.K_q]:
        x += (64 * 7)
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[7].play()
        elif (instrument is 'guitar'):
            guitarSounds[7].play()
        elif (instrument is 'electric'):
            electricSounds[7].play()
        elif (instrument is 'bass'):
            bassSounds[7].play()
        elif (instrument is 'Saxophone'):
            saxSounds[7].play()
    if keys[pygame.K_w]:
        x += (64 * 8)
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[8].play()
        elif (instrument is 'guitar'):
            guitarSounds[8].play()
        elif (instrument is 'electric'):
            electricSounds[8].play()
        elif (instrument is 'bass'):
            bassSounds[8].play()
        elif (instrument is 'Saxophone'):
            saxSounds[8].play()
    if keys[pygame.K_e]:
        x += (64 * 9)
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[9].play()
        elif (instrument is 'guitar'):
            guitarSounds[9].play()
        elif (instrument is 'electric'):
            electricSounds[9].play()
        elif (instrument is 'bass'):
            bassSounds[9].play()
        elif (instrument is 'Saxophone'):
            saxSounds[9].play()
    if keys[pygame.K_r]:
        x += (64 * 10)
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[10].play()
        elif (instrument is 'guitar'):
            guitarSounds[10].play()
        elif (instrument is 'electric'):
            electricSounds[10].play()
        elif (instrument is 'bass'):
            bassSounds[10].play()
        elif (instrument is 'Saxophone'):
            saxSounds[10].play()
    if keys[pygame.K_t]:
        x += (64 * 11)
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[11].play()
        elif (instrument is 'guitar'):
            guitarSounds[11].play()
        elif (instrument is 'electric'):
            electricSounds[11].play()
        elif (instrument is 'bass'):
            bassSounds[11].play()
        elif (instrument is 'Saxophone'):
            saxSounds[11].play()
    if keys[pygame.K_y]:
        x += (64 * 12)
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[12].play()
        elif (instrument is 'guitar'):
            guitarSounds[12].play()
        elif (instrument is 'electric'):
            electricSounds[12].play()
        elif (instrument is 'bass'):
            bassSounds[12].play()
        elif (instrument is 'Saxophone'):
            saxSounds[12].play()
    if keys[pygame.K_u]:
        x += (64 * 13)
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[13].play()
        elif (instrument is 'guitar'):
            guitarSounds[13].play()
        elif (instrument is 'electric'):
            electricSounds[13].play()
        elif (instrument is 'bass'):
            bassSounds[13].play()
        elif (instrument is 'Saxophone'):
            saxSounds[13].play()
    if keys[pygame.K_i]:
        x += (64 * 14)
        #highlightKey()
        if (instrument is 'piano'):
            pianoSounds[14].play()
        elif (instrument is 'guitar'):
            guitarSounds[14].play()
        elif (instrument is 'electric'):
            electricSounds[14].play()
        elif (instrument is 'bass'):
            bassSounds[14].play()
        elif (instrument is 'Saxophone'):
            saxSounds[14].play()
    
    time.sleep(0.075)
    x = 141
    redrawGamewindow()


#playSong(happy_bday, 'guitar')
