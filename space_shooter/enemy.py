import pygame
import random
from utils import COLORS, ASSETS


class Enemy:
    def __init__(self, x, y, d, type_="fast"):
        self.x = x
        self.y = y
        self.d = d
        self.type = type_
        self.speed = random.uniform(3, 5) if type_ == "fast" else random.uniform(1, 3)  # Speed variation
        self.dodge_cooldown = 0
        self.img = ASSETS["enemy1_img"] if type_ == "fast" else ASSETS["enemy2_img"]

    def draw(self, display):
        if self.img:
            display.blit(self.img, (self.x, self.y))
        else:
            pygame.draw.ellipse(display, COLORS["green"] if self.type == "fast" else (0, 255, 0), (self.x, self.y, self.d, self.d))
            pygame.draw.ellipse(display, COLORS["dark_gray"], (self.x + 10, self.y + self.d / 3, 8, 8), 2)
            pygame.draw.ellipse(display, COLORS["dark_gray"], (self.x + self.d - 20, self.y + self.d / 3, 8, 8), 2)
            pygame.draw.rect(display, COLORS["dark_gray"], (self.x, self.y + self.d - 20, 50, 7))

    # AI: Chase player
    def move(self, player_x):
        if self.x + self.d // 2 < player_x:
            self.x += min(self.speed, abs(player_x - self.x))
        elif self.x + self.d // 2 > player_x:
            self.x -= min(self.speed, abs(player_x - self.x))

        # Enemies move down slowly
        self.y += self.speed / 2

    def dodge(self, bullets):
        if self.type == "dodger" and self.dodge_cooldown <= 0:
            for bullet in bullets:
                if abs(bullet.x - self.x) < 50 and self.y - 30 < bullet.y < self.y + self.d + 30:
                    if bullet.x < self.x:
                        self.x += 40
                    else:
                        self.x -= 40
                    self.dodge_cooldown = 20
                    break
        else:
            self.dodge_cooldown -= 1

    def shift_down(self):
        self.y += self.d
