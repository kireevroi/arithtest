import sqlite3

# инциализируем базу данных, если её еще не было.
def dbinit(db_name):
    db_connection = sqlite3.connect(db_name)
    db_cursor = db_connection.cursor()

    db_cursor.execute('''
              CREATE TABLE IF NOT EXISTS statistics
              ([user_id] INTEGER PRIMARY KEY, [user_name] TEXT, [score] INTEGER)
              ''')

    db_connection.commit()
    return "База данных " + str(db_name) + " инициализирована!"

# добавление значений в базу данных
def dbappend(db_name, name, score):
    db_connection = sqlite3.connect(db_name)
    db_cursor = db_connection.cursor()

    db_cursor.execute(('''
                INSERT INTO statistics (user_id, user_name, score) VALUES (NULL, ?, ?)
                '''), (name, score))
    db_connection.commit()
    return print("Молодец, " + str(name) + "! Ты заработал(а) "+str(score)+" очков!!!")
# печать таблицы лидеров
def db_print(db_name):
    db_connection = sqlite3.connect(db_name)
    db_cursor = db_connection.cursor()
    db_cursor.execute('''SELECT user_name, score FROM statistics ORDER BY score LIMIT 5''')
    for i in db_cursor.fetchall():
        print(i) # заменить на cool_text

    db_connection.commit()


#тесты    
dbinit('db_stats')
dbappend('db_stats', 'Рома', 100)
db_print('db_stats')
