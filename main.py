# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

play = True

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    game_lope(screen)
    print("Ending asteroids!")



def game_lope(screen):
    while play:
        handel_Inputs()
        if not play:
            return
        
        screen.fill(0)
        pygame.display.flip()


def handel_Inputs():
    handel_Window_Inputs()

def handel_Window_Inputs():
    global play
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            return

if __name__ == "__main__":
    main()