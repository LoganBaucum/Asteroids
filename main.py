import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0.0
    running = True

    while running:
        log_state()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return

        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
