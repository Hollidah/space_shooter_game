import pygame
from utils import COLORS


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = 10
        self.speed = -5   # move upward

    def draw(self, display):
        pygame.draw.ellipse(display, COLORS["orange"], (self.x, self.y, self.d, self.d))

    def move(self):
        self.y += self.speed

    def hit(self, x, y, d):
        if x < self.x < x + d:
            if y + d > self.y > y:
                return True

