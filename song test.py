#from playsound import playsound
import pygame, time
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")
x = 50
y = 50
width = 2000
height = 1000
vel = 5 
run = True
left = False
right = False
isjump = False
jcount = 0
walknum = 0

#musical components
rest = 'rest'
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

def playSong(song, instrument):
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

#############################################################################################################################################################

while run:
    instrument = 'guitar'
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if (instrument is 'piano'):
            pianoSounds[0].play()
        elif (instrument is 'guitar'):
            guitarSounds[0].play()
    if keys[pygame.K_s]:
        if (instrument is 'piano'):
            pianoSounds[1].play()
        elif (instrument is 'guitar'):
            guitarSounds[1].play()
    if keys[pygame.K_d]:
        if (instrument is 'piano'):
            pianoSounds[2].play()
        elif (instrument is 'guitar'):
            guitarSounds[2].play()
    if keys[pygame.K_f]:
        if (instrument is 'piano'):
            pianoSounds[3].play()
        elif (instrument is 'guitar'):
            guitarSounds[3].play()
    if keys[pygame.K_g]:
        if (instrument is 'piano'):
            pianoSounds[4].play()
        elif (instrument is 'guitar'):
            guitarSounds[4].play()
    if keys[pygame.K_h]:
        if (instrument is 'piano'):
            pianoSounds[5].play()
        elif (instrument is 'guitar'):
            guitarSounds[5].play()
    if keys[pygame.K_j]:
        if (instrument is 'piano'):
            pianoSounds[6].play()
        elif (instrument is 'guitar'):
            guitarSounds[6].play()
    if keys[pygame.K_q]:
        if (instrument is 'piano'):
            pianoSounds[7].play()
        elif (instrument is 'guitar'):
            guitarSounds[7].play()
    if keys[pygame.K_w]:
        if (instrument is 'piano'):
            pianoSounds[8].play()
        elif (instrument is 'guitar'):
            guitarSounds[8].play()
    if keys[pygame.K_e]:
        if (instrument is 'piano'):
            pianoSounds[9].play()
        elif (instrument is 'guitar'):
            guitarSounds[9].play()
    if keys[pygame.K_r]:
        if (instrument is 'piano'):
            pianoSounds[10].play()
        elif (instrument is 'guitar'):
            guitarSounds[10].play()
    if keys[pygame.K_t]:
        if (instrument is 'piano'):
            pianoSounds[11].play()
        elif (instrument is 'guitar'):
            guitarSounds[11].play()
    if keys[pygame.K_y]:
        if (instrument is 'piano'):
            pianoSounds[12].play()
        elif (instrument is 'guitar'):
            guitarSounds[12].play()
    if keys[pygame.K_u]:
        if (instrument is 'piano'):
            pianoSounds[13].play()
        elif (instrument is 'guitar'):
            guitarSounds[13].play()
    if keys[pygame.K_i]:
        if (instrument is 'piano'):
            pianoSounds[14].play()
        elif (instrument is 'guitar'):
            guitarSounds[14].play()

#playSong(happy_bday, 'guitar')
#playSong(twinkle, 'piano')