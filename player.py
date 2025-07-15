import circleshape as circle
import constants as const
import pygame

class Player(circle.CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, const.PLAYER_RADIUS)
        self.rotation = 0       

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += const.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= const.PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += const.PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            shot = Shot(self.position.x, self.position.y, self.rotation)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * const.PLAYER_SHOOT_SPEED
         
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * const.PLAYER_SPEED * dt

    def shoot(self):
        return Shot(self.position.x, self.position.y, self.rotation)

class Shot(circle.CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, const.SHOT_RADIUS)
        direction = pygame.Vector2(0, 1).rotate(rotation)
        start_pos = pygame.Vector2(x, y) + direction * const.PLAYER_RADIUS
        self.velocity = direction * const.PLAYER_SHOOT_SPEED
        self.position = start_pos
           
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
        
        