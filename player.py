import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) #calls parent constructor
        self.rotation = 0 #initialize rotation

    def triangle(self):
        """Returns the three points defining the player's triangle shape."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Draw the player as a white triangle on the screen."""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)