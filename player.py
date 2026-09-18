import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.rotation: float = 0
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

    # Player is represented as a triangle but has a hitbox of a circle.
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, delta_time: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def update(self, delta_time: float) -> None:
        self.shot_cooldown = max(0, self.shot_cooldown - delta_time)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(delta_time * -1.0)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(delta_time * -1.0)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, delta_time: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * delta_time
        self.position += rotated_with_speed_vector

    def shoot(self) -> None:
        if self.shot_cooldown == 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
