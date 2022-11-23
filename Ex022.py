#Faça um programa em python que abre e reproduza o áudio de um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('Ex022.mp3')
pygame.mixer.music.play()
pygame.event.wait()
