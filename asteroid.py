import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def split(self) -> None:
        self.kill()

        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20, 50)
            vel_1 = self.velocity.rotate(rand_angle)
            vel_2 = self.velocity.rotate(rand_angle * -1.0)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = vel_1 * 1.2
            new_asteroid_2.velocity = vel_2 * 1.2

    def update(self, delta_time: float) -> None:
        self.position += self.velocity * delta_time
