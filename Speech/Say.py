from gtts import gTTS
import pygame
import os

def say(Text):

    g = gTTS(text=Text, tld='co.uk', lang='en', slow=False)

    g.save('C:\\Users\\paruk\\Desktop\\AI\\Speech\\Current.mp3')

    

    pygame.mixer.init()


    pygame.mixer.music.load('C:\\Users\\paruk\\Desktop\\AI\\Speech\\Current.mp3')


    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        print()
    