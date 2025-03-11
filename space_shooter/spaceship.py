import pygame
from utils import COLORS, ASSETS

class Spaceship:
    def__init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def draw(self, display):
        if ASSETS["ship_img"]:
            display.blit(ASSETS["ship_img"], (self.x, self.y))
        else:
            pygame.draw..rect(display, COLORS["yellow"], (self.x + self.w/2 - 8, self.y - 10, 16, 10))
            pygame.draw.rect(display, self.colour, (self.x, self.y, self.w, self.h))
            pygame.draw.rect(display, COLORS["dark_gray"], (self.x + 5, self.y + 6, 10, self.h - 10))
            pygame.draw.rect(display, COLORS["dark_gray"], (self.x + self.w - 15, self.y + 6, 10, self.h - 10))