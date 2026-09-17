import pygame

from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0.0
    frame_rate = 60
    running = True

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    # Game Loop
    while running:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

        screen.fill("black")

        updatable.update(delta_time)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        delta_time = clock.tick(frame_rate) / 1000


if __name__ == "__main__":
    main()
