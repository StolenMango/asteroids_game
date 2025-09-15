from circleshape import *

Class Player(CircleShape):
    def __init__(self, x, y, rotation):
    super()def __init__(x, y)
    self.rotation = 0

# player will look like a triangle, even though we'll use a circle to represent its hitbox
def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]