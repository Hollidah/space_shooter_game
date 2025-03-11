# Space Shooter Game 🚀

A simple 2D game built using Python and Pygame. The game challenges players to defend space by controlling a spaceship, shooting down invading enemies, and surviving as long as possible. 

The game also integrates AI for smarter enemy movement and a database for storing high scores.This game includes:
    - Player movement and shooting
    - Enemy/Alien movement integerated with AI
    - Bullet collision detection
    - Databse integration to handle CRUD operations

# Objective
Destroy all aliens before they reach the bottom of the screen to win.
Avoid letting any alien cross the bottom boundary, or the game ends in defeat.

# Controls
Left and Right Arrow Keys: To move the spaceship
Spacebar: To shoot bullets
Game Over: If an enemy reaches the bottom of the screen.
Win: Defeat all waves of enemies.
Q: Quit game

# Scoring
Each alien destroyed awards 10 points.
After winning or losing, enter your name (via console) to save your score, then view the top 5 scores on-screen.


# Features
CRUD: Scores saved in an SQLite database  (game_scores.db) and displayed in-game after win/loss.

AI: Two alien types enhanced with AI:
    1. Fast Aliens: They move at high speed and can not dodge bullets.
    2. Dodger Aliens: They move at a slower speed and can dodge bullets.

Score system: Earn 10 points per alien hit, with scores saved to database and displayes in-game after a win or loss.

Graphics/Sound: Custom images and sound effects (with fallbacks).

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
    - Save scores after each game.
    - Retrieve top high scores for display.

# How to play
    1. Launch game.py.
    2. Use arrow keys to move your spaceship and Spacebar to shoot.
    3. Destroy all 8 aliens to win, or lose if any reach the bottom.
    4. After the game ends, enter your name in the console to save your score.
    5. View the top 5 scores on-screen for 5 seconds before the game exits.

# Potential Enhancements
    1. In-Game Name Input: Replace console input with an on-screen text box using Pygame’s key events.
    2. More Alien Types: Add aliens that shoot back or move in patterns.
    3. Levels: Introduce waves with increasing difficulty (more aliens, faster speeds).
    4. Visual Effects: Add explosions or particle effects on hits.
    5. Main Menu: Include a start screen with options to view scores or quit

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Author
Hollidah Chemutai
    

Copyrights: 2025