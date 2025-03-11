import sqlite3

# Connect to database
def init_db():
    conn = sqlite3.connect("game_scores.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        player_name TEXT,
                        score INTEGER)''')
    conn.commit()
    conn.close()


# Saves player's scores 
def save_score(player_name, score):
    conn = sqlite3.connect("game_scores.db")    # create a new connection
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (player_name, score) VALUES (?, ?)", (player_name, score))
    conn.commit()
    conn.close()


# Retrieves the top 5 scores
def get_high_score():
    conn = sqlite3.connect("game_scores.db")
    cursor = conn.cursor()
    cursor.execute("SELECT player_name, score FROM scores ORDER BY score DESC LIMIT 5")
    scores = cursor.fetchall()
    conn.close()
    return scores

init_db()      # Initialize database 


# Saving scores
save_score("Hollidah", 150)
save_score("Player2", 200)

# Retriving scores
high_scores = get_high_score()
for name, score in high_scores:
    print(f"{name}: {score}")
