import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('F:\MSC\On Repeat\TTNG - Gibbon.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()