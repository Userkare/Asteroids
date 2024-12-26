from circleshape import *
from constants import *
from Shot import Shot


class Player(CircleShape):

    timer = 0

    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(),2)

    def rotat(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shoot = Shot(self.position.x, self.position.y)
        new_shoot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotat( -dt)
        if keys[pygame.K_d]:
            self.rotat( dt)

        if(keys[pygame.K_w]):
            self.move(dt)
        if(keys[pygame.K_s]):
            self.move(-dt)

        if(keys[pygame.K_SPACE]):
            if self.timer < 0:
                self.timer = PLAYER_SHOOT_COOLDOWN
                self.shoot()
