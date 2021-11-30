import sqlite3

#initializing database
def dbinit(db_name):
    db_connection = sqlite3.connect(db_name)
    db_cursor = db_connection.cursor()

    db_cursor.execute('''
              CREATE TABLE IF NOT EXISTS statistics
              ([user_id] INTEGER PRIMARY KEY, [user_name] TEXT, [score] INTEGER)
              ''')

    db_connection.commit()
    print("База данных " + str(db_name) + " инициализирована!")
    return None

#appending values to database
def dbappend(db_name, name, score):
    db_connection = sqlite3.connect(db_name)
    db_cursor = db_connection.cursor()

    db_cursor.execute(('''
                INSERT INTO statistics (user_id, user_name, score) VALUES (NULL, ?, ?)
                '''), (name, score))
    db_connection.commit()
    print("Молодец, " + str(name) + "! Ты заработал(а) "+str(score)+" очков!!!")
    return None

#printing leaderboard
def dbprint(db_name):
    db_connection = sqlite3.connect(db_name)
    db_cursor = db_connection.cursor()
    db_cursor.execute('''SELECT user_name, score FROM statistics ORDER BY score DESC LIMIT 5''')
    for i in db_cursor.fetchall():
        print(i) #should replace with cooltext

    db_connection.commit()
    return None
