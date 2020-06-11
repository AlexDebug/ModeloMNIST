from pygame.locals import *
import pygame
import sys 

HEIGHT = 64
WIDTH  = 64

display = pygame.display.set_mode((HEIGHT, WIDTH))

while True:
    
    events = pygame.event.get()

    for event in events:
        if event.type == QUIT:
            sys.exit()