import os 
import sys
import sqlite3
import json
import pandas as pd

class Database():
    def __init__(self, path):
        self.path = path
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
    
    def disconnect(self):
        self.connection.commit()
        self.connection.close()
    
    def execute(self, request):
        self.cursor.execute(request) 

    def dbtabel_to_df(self, name):
        self.execute(f'SELECT * FROM {name}')
        lst = self.cursor.fetchall()
        return pd.DataFrame(lst, columns=[c[0] for c in self.cursor.description])

    #Metod to add something from json to motherbase


def extract_stats(name):
    db = Database(f'data\characters\{name}.db')
    Cyberneticks = db.dbtabel_to_df('Cyberneticks')
    Gear = db.dbtabel_to_df('Gear')
    Health = db.dbtabel_to_df('Health')
    Info = db.dbtabel_to_df('Info')
    Stats = db.dbtabel_to_df('Stats')
    Weapons = db.dbtabel_to_df('Weapons')
    data = {'Cyberneticks': Cyberneticks, 'Gear': Gear, 'Health': Health, 'Info': Info, 'Stats': Stats, 'Weapons': Weapons}
    db.disconnect()
    return data

def show_stat(from_where, name):
    return (from_where[from_where['name'] == name].values[0])[1]

#Create a new db for character
def create_new_character(name):
    connection = sqlite3.connect(f'data/characters/{name}.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE Cyberneticks (
        id       INTEGER PRIMARY KEY,
        name     TEXT    NOT NULL,
        humanity INTEGER,
        cost     INTEGER
        );
        ''')        

    cursor.execute('''
        CREATE TABLE Gear (
        id       INTEGER PRIMARY KEY,
        name     TEXT    NOT NULL,
        class    TEXT    NOT NULL,
        price    INTEGER,
        quantity INTEGER
        );
        ''')        

    cursor.execute('''
        CREATE TABLE Health (
        id    INTEGER PRIMARY KEY,
        limb  TEXT    NOT NULL,
        armor INTEGER,
        SDP   INTEGER
        );
        ''')        

    cursor.execute('''
        CREATE TABLE Info (
        link_to_story TEXT PRIMARY KEY,
        Role          TEXT,
        name          TEXT
        );
        ''')        

    cursor.execute('''
        CREATE TABLE Stats (
        name TEXT NOT NULL PRIMARY KEY,
        stat INTEGER
        );
        ''')        

    cursor.execute('''
        CREATE TABLE Weapons (
        id           INTEGER PRIMARY KEY,
        name         TEXT    NOT NULL,
        type         TEXT    NOT NULL,
        accuracy     INTEGER,
        stealthiness INTEGER,
        availability TEXT    NOT NULL,
        damage       TEXT    NOT NULL,
        bullet_type  TEXT    NOT NULL,
        ammo         INTEGER,
        ROF          INTEGER
        );
       ''')        

    connection.commit()
    connection.close()


def json_to_Motherbase(self, path_to_json, name, source='CP20'):
    dll = []
    with open(path_to_json, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        for i in data['items']:
            dll.append(i)

    df = pd.DataFrame(dll)
    try:
        del df['img1']
    except:
        pass
    try:
        del df['img2']
    except:
        pass
    try:
        del df['CATEGORY']
    except:
        pass
    try:
        del df['Pg']
    except:
        pass
    df = df[df['Source'] == source]
    del df['Source']
    df.to_sql(name, self.connection, index=False)


def names():
    names = os.listdir('data\characters')
    actual_name = []
    for i in names:
        actual_name.append(i[:-3])
    return actual_name