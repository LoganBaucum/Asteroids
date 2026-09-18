import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, LINE_WIDTH)

    def update(self, delta_time: float):
        self.velocity += self.velocity * delta_time
