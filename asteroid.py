import circleshape as circle
import pygame
import constants as const
import random

class Asteroid(circle.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= const.ASTEROID_MIN_RADIUS:
            return
        else:
            self.random_angle = random.uniform(20, 50)
            self.new_radius = self.radius - const.ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position[0], self.position[1], self.new_radius)
            new_asteroid2 = Asteroid(self.position[0], self.position[1], self.new_radius)
            new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, self.random_angle)*1.2
            new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -self.random_angle)*1.2
        return new_asteroid1, new_asteroid2

        
        