# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable,)
Shot.containers = (updatable, drawable, shots)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill("black")
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)
        # --- collision detection ---
        for asteroid in asteroids:
            if player.checkCollision(asteroid):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.checkCollision(asteroid):
                    asteroid.split()
                    shot.kill()
        # ---------------------------
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000  # in seconds

if __name__ == "__main__":
    main()