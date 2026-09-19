import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    MAX_DELTA_TIME,
    MAX_FPS,
    PLAYER_RADIUS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0.0
    running = True

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable
    Player.containers = (drawable, updatable)
    Shot.containers = (drawable, shots, updatable)

    AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    # Game Loop
    try:
        while running:
            log_state()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for update_obj in updatable:
                update_obj.update(delta_time)

            for asteroid in asteroids.sprites():
                if asteroid.collides_with(player):
                    log_event("player_hit")
                    print("Game over!")
                    running = False

                for shot in shots:
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        shot.kill()
                        asteroid.split()
                        break

            screen.fill("black")
            for draw_obj in drawable:
                draw_obj.draw(screen)
            pygame.display.flip()

            delta_time = min(clock.tick(MAX_FPS) / 1000, MAX_DELTA_TIME)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
