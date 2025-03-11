# Space Shooter Game 🚀

A simple 2D game built using Python and Pygame. The game challenges players to defend space by controlling a spaceship, shooting down invading enemies, and surviving as long as possible. The game also integrates AI for smarter enemy movement and a database for storing high scores.This game includes:
    - Player movement and shooting
    - Enemy/Alien movement integerated with AI
    - Bullet collision detection
    - Databse integration to handle CRUD operations





# Features
CRUD: Scores saved in an SQLite database  (game_scores.db) and displayed in-game after win/loss.

AI: Two alien types enhanced with AI:
    1. Fast Aliens: They move at high speed and can not dodge bullets.
    2. Dodger Aliens: They move at a slower speed and can dodge bullets.

Score system: Earn 10 points per alien hit, with scores saved to database and displayes in-game after a win or loss.

Graphics/Sound: Custom images and sound effects (with fallbacks).

# Controls and how to play
Left and Right Arrow Keys: To move the spaceship

Spacebar: To shoot bullets

Objective: Destroy all enemies before they reach the bottom.

Game Over: If an enemy reaches the bottom of the screen.

Win: Defeat all waves of enemies.

Q: Quit game

# Project Structure
    game.py: Main game loop
    spaceship.py: Spaceship logic
    enemy.py: Alien logic
    bullet.py: Bullet logic
    database.py: Handles CRUD operations
    utils.py: Shared utilities (colors, assets)
    assets/: Store images and sounds

# Database Integration
This project includes an SQLite database to store high scores. The database is managed via database.py, and it performs the following functions:

Save scores after each game.

Retrieve top high scores for display.


# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Author
     Hollidah Chemutai
    

                                Copyrights: 2025