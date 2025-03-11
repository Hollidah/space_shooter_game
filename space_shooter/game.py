import pygame
import sys
import time
from spaceship import SpaceShip
from enemy import Enemy
from bullet import Bullet
from database import init_db, save_score, get_high_score
from utils import load_assets, COLORS



# Initialization 
pygame.init()
pygame.mixer.init()

# Screen settings
width = 700
height = 500

display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Shooter")

ship_width = 40
ship_height = 30


def saved(score):
    font = pygame.font.SysFont("Wide Latin", 22)
    font_large = pygame.font.SysFont("Wide Latin", 43)
    
    text2 = font_large.render("Congratulations!", True, COLORS["white1"])
    text = font.render("You prevented Alien Invasion!", True, COLORS["white1"])

    player_name = input("Enter your name:")
    save_score(player_name, score)
    scores = get_high_score()
    
    display.fill(COLORS["background"])
    display.blit(text2, (60, height/2 - 100))
    display.blit(text, (45, height/2 - 50))
    score_font = pygame.font.SysFont("Arial", 20)

    for i, (name, s) in enumerate(scores):
        score_text = score_font.render(f"{name}: {s}", True, COLORS["white1"])
        display.blit(score_text, (width/2 - 50, height/2 + i * 30))
    
    pygame.display.update()
    time.sleep(5)


def game_over(score):
    font = pygame.font.SysFont("Chiller", 50)
    font_large = pygame.font.SysFont("Chiller", 100)
   
    text2 = font_large.render("Game Over!", True, COLORS["white1"])
    text = font.render("You Could not Prevent the Alien Invasion!", True, COLORS["white1"])

    player_name = input("Enter your name: ")
    save_score(player_name, score)
    scores = get_high_score()

    display.fill(COLORS["background"])
    display.blit(text2, (180, width/2 - 100))
    display.blit(text, (45, height/2 - 50))  
    score_font = pygame.font.SysFont("Arial", 20) 

    for i, (name, s) in enumerate(scores):
        score_text = score_font.render(f"{name}: {s}", True, COLORS["white1"])
        display.blit(score_text, (width/2 - 50, height/2 + i * 30))

        pygame.display.update()
        time.sleep(5)
        


def game():
    init_db()
    invasion = False
    ship = SpaceShip(width/2 - ship_width/2, height - ship_height - 10, ship_width, ship_height, COLORS["white"]) 
    bullets = []
    enemies = []
    num_enemies = 8
    d = 50 
    score = 0


    for i in range(num_enemies):
        enemy_type = "fast" if i % 2 == 0 else "dodger"
        enemies.append(Enemy((i+1)*d + i*20, d+20, d, enemy_type)) 

    while not invasion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.x +=5
                if event.key == pygame.K_LEFT:
                    ship.x -=5
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(ship.x + ship_width/2 - 5, ship.y))
                    if ASSETS["shoot_sound"]:
                        ASSETS["shoot_sound"].play()

        display.fill(COLORS["background"])

        for bullet in bullets[:]:
            bullet.move()
            bullet.draw(display)
            if bullet.y < 0:
                bullets.remove(bullet)

     # Check for collisions
        for enemy in enemies[:]:
            enemy.move(ship.x + ship_width/2)
            enemy.dodge(bullets)
            enemy.draw(display)

            for bullet in bullets[:]:
                if bullet.hit(enemy.x, enemy.y, enemy.d):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 10
                    if ASSETS["hit_sound"]:
                        ASSETS["hit_sound"].play()
                    break

        if not enemies:
            saved(score)
            invasion = True
            
        for enemy in enemies:
            if enemy.y + enemy.d > height:
                game_over(score)
                invasion = True
                break

        ship.x = max(0, min(ship.x, width - ship_width))
        ship.draw(display)

        font = pygame.font.SysFont("Arial", 20)
        score_text = font.render(f"Score: {score}", True, COLORS["white1"])
        display.blit(score_text, (10,10))

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    ASSETS = load_assets()
    game()

