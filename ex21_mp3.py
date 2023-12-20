#tocando um mp3
import pygame
#inicializando o modulo:
pygame.init()
#comandos para tocar audios em si
pygame.mixer.music.load('numb.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()