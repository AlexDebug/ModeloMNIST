from pygame.locals import *
import pygame
import sys 

HEIGHT = 500
WIDTH  = 500

display = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.draw.rect(display, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
while True:
    
    events = pygame.event.get()

    for event in events:
        if event.type == QUIT:
            sys.exit()

   
    
    click, _, _ = pygame.mouse.get_pressed()
    if click:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(display, (255,255,255), pos, 10)

    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        pygame.draw.rect(display, (0, 0, 0), (0, 0, WIDTH, HEIGHT))

    pygame.display.flip()