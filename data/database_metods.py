import sqlite3


def create_new_character(name):
    connection = sqlite3.connect(f'characters\{name}.db')
    cursor = connection.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Gear(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        class TEXT NOT NULL,
        price INTEGER,
        quantity INTEGER
        )
        ''')        

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Weapons(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        accuracy INTEGER,
        stealthiness INTEGER,
        availability TEXT NOT NULL,
        damage TEXT NOT NULL,
        bullet_type TEXT NOT NULL,
        ammo INTEGER,
        ROF INTEGER
        )
        ''')        

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cyberneticks(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        humanity INTEGER,
        cost INTEGER
        )
        ''')        

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Stats(
        name TEXT NOT NULL PRIMARY KEY,
        previous_stat INTEGER,
        actual_stat INTEGER
        )
        ''')        

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Balance(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        money INTEGER,
        op_type INTEGER
        )
        ''')        

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Health(
        id INTEGER PRIMARY KEY,
        limb TEXT NOT NULL,
        armor INTEGER,
        SDP INTEGER
        )
        ''')        

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Story(
        link TEXT NOT NULL PRIMARY KEY
        )
        ''')
    
    connection.commit()
    connection.close()