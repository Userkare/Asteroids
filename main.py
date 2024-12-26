import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from Shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField ()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for updatable_thing in updatable:
            updatable_thing.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collison(shot):
                    asteroid.kill()
                    shot.kill()
                
            

        for asteroid in asteroids:
            if asteroid.collison(player):
                print("Game over!")
                return

        screen.fill("black")      

        for drawable_thing in drawable:
            drawable_thing.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
