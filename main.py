import sys
import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()

# Window Setup
gameWindow = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("EvoVikings")

gameRunning = True

# GAME LOOP
while gameRunning:
    # EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    # CONTENT
    gameWindow.fill((0, 0, 0))

    # UPDATE
    pygame.display.update()


# release memory
pygame.quit()
sys.exit()
