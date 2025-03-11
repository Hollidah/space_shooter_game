import pygame

#class Player:
   # def __init__(self, x, y, w, h, colour):
        #self.x = x
        #self.y = y
        #self.w = w
        #self.h = h
        #self.colour = colour

   # def draw(self):
        #pygame.draw.rect(display, yellow, (self.x + self.w/2 - 8, self.y - 10, 16, 10))
        #pygame.draw.rect(display, self.colour, (self.x, self.y, self.w, self.h))
        #pygame.draw.rect(display, dark_gray, (self.x + 5, self.y + 6, 10, self.h - 10))
        #pygame.draw.rect(display, dark_gray, (self.x + self.w - 15, self.y + 6, 10, self.h - 10))


COLORS = {
     "background": (74, 35, 90),
     "white": (244, 246, 247),
     "yellow": (241, 196, 15),
     "orange": (186, 74, 0),
     "green": (35, 155, 86),
     "white1": (253, 254, 254),
     "dark_gray": (23, 32, 42)
}

def load_assets():
     try:
          ship_img = pygame.image.load("assets/ship.png").convert_alpha()
          ship_img = pygame.transform.scale(ship_img, (40, 30))

          enemy1_img = pygame.image.load("assets/enemy1.png").convert_alpha()
          enemy1_img = pygame.transform.scale(enemy1_img, (50, 50))

          enemy2_img = pygame.image.load("assets/enemy2.png").convert_alpha()
          enemy2_img = pygame.transform.scale(enemy2_img, (50, 50))
          
          shoot_sound = pygame.mixer.Sound("assets/shoot.wav")
          hit_sound = pygame.mixer.Sound("assets/hit.wav")

     except:
          ship_img = enemy1_img = enemy2_img = shoot_sound = hit_sound = None
     return{
          "ship_img": ship_img,
          "enemy1_img": enemy1_img,
          "enemy2_img": enemy2_img,
          "shoot_sound": shoot_sound,
          "hit_sound": hit_sound
     }   

ASSETS = load_assets()