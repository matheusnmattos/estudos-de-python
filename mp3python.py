import pygame
import time

pygame.init()

pygame.mixer.music.load("nocturne.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()
time.sleep(60)