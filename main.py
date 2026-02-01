import sys
import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # set fps of the game
    clock = pygame.time.Clock()
    dt = 0
    
    # adding groups
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # creating an instance of player 
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # group for the asteroids AsteroidField
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()

    Shot.containers = (shots,updatable, drawable)

    while True:
        # print("hi")
        log_state()
        for event in pygame.event.get():
            # implemente l'action de quitter la fenetre en cliquant sur le btn quitter
            if event.type == pygame.QUIT:
                pygame.quit()
                return
                        
        updatable.update(dt)
        
        for a in asteroids:
            for shot in shots:
                if shot.collides_with(a):
                    log_event("asteroid_shot")
                    a.split()
                    shot.kill()
                if a.collides_with(player):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()

        screen.fill("black")  
        
        # draw the drawable thing
        for i in drawable:
            i.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
