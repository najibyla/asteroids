import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        print("hi")
        log_state()
        for event in pygame.event.get():
            # implemente l'action de quitter la fenetre en cliquant sur le btn quitter
            if event.type == pygame.QUIT:
                return False
            
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
