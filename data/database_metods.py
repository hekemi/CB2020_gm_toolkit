import sqlite3
import json
import pandas as pd

class Db():
    def __init__(self, path):
        self.path = path
        self.connection = sqlite3.connect(path)

    def connect(self):
        return self.connection.cursor()
    
    def disconnect(self):
        self.connection.commit()
        self.connection.close()


    def create_new_character(name, cursor):

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


    def json_to_df_to_Motherbase(path, name, connection):
        dll = []
        with open(path, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
            for i in data['items']:
                dll.append(i)

        df = pd.DataFrame(dll)
        del df['img1']
        del df['img2']
        del df['CATEGORY']
        try:
            del df['Pg']
        except:
            pass
        df = df[df['Source'] == 'CP20']
        del df['Source']
        df.to_sql(name, connection, index=False)