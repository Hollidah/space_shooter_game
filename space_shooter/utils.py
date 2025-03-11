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
          alien1_img = pygame.image.load("assets/alien1.png").convert_alpha()
          alien1_img = pygame.transform.scale(alien1_img, (50, 50))
          alien2_img = pygame.image.load("assets/alien2.png").convert_alpha()
          alien2_img = pygame.transform.scale(alien2_img, (50, 50))
          shoot_sound = pygame.mixer.Sound("assets/shoot.wav")
          hit_sound = pygame.mixer.Sound("assets/hit.wav")

     except:
          ship_img = alien1_img = alien2_img = shoot_sound = hit_sound = None
     return{
          "ship_img": ship_img,
          "alien1_img": alien1_img,
          "alien2_img": alien2_img,
          "shoot_sound": shoot_sound,
          "hit_sound": hit_sound
     }   