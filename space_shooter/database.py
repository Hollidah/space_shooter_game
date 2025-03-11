import sqlite3

# Connect to database
conn = sqlite3.connect("game_scores.db")
cursor = conn.cursor()

# Creates a tble if it does not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    player_name TEXT,
                    score INTEGER)''')
conn.commit()


# Saves players scores into the database
def save_score(player_name, score):
    cursor.execute("INSERT INTO scores (player_name, score) VALUES (?, ?)", (player_name, score))
    conn.commit()

# Retrieves the top 5 scores
def get_high_score():
    cursor.execute(""SELECT player_name, score FROM scores ORDER BY score DESC LIMIT 5"")
    return cursor.fetchall

conn.close()