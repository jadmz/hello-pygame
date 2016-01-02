import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()
pygame.key.set_repeat(1, 10)

# set up the window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up fonts
basicFont = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
deltat = clock.tick(FRAMES_PER_SECOND)

windowSurface.fill(GREEN)
posx = 100
posy = 100
width = 50
height = 50

# draw the text's background rectangle onto the surface
windowSurface.fill(RED, (posx, posy, width, height))

pygame.display.update()


# run the game loopn
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif hasattr(event, 'key') and event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                posx += 1
            elif event.key == K_LEFT:
                posx -= 1
            elif event.key == K_DOWN:
                posy += 1
            elif event.key == K_UP:
                posy -= 1

    windowSurface.fill(GREEN)

    posx = posx if posx > 0 else 0
    posx = posx if posx+width < windowSurface.get_width() else windowSurface.get_width()- width
    posy = posy if posy > 0 else 0
    posy = posy if posy + height < windowSurface.get_height() else  windowSurface.get_height() - height
    rect = (posx, posy, width, height)
    windowSurface.fill(RED, rect)
    pygame.display.flip()
                   
        
