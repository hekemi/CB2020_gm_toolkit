import sqlite3
import json


def create_new_character(name):
    connection = sqlite3.connect(f'data\characters\{name}.db')
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


# That function need to be rewriteted to use in real code so pay attention
# + u need to create a table first
# so i just will ctrl+c ctrl+v when needed
def add_table_to_Motherbase(file_name):
    dll = []
    with open(f'data\jsons\{file_name}.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        for i in data['items']:
            if i['Cost'] == '':
                dll.append([i['Name'], i['TYPE'], 'set by gm'])
                continue
            dll.append([i['Name'], i['TYPE'], i['Cost']])



    connection = sqlite3.connect('data\Motherbase.db')
    cursor = connection.cursor()

    for i in dll:
        cursor.execute(f'INSERT INTO {file_name} (name, category, cost) VALUES (?, ?, ?)', (i[0], i[1], i[2]))

    connection.commit()
    connection.close()