import sqlite3
import database_metods as db_m
import json

connection = sqlite3.connect('data\Motherbase.db')
cursor = connection.cursor()

file_name = 'Equipment'
dll = []
with open(f'data\jsons\{file_name}.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
    for i in data['items']:
        if i['Source'] == 'CP20':
            if i['Cost'] == '':
                dll.append([i['Name'], i['TYPE'], 'set by gm', i['Notes']])
                continue
            dll.append([i['Name'], i['TYPE'], i['Cost'], i['Notes']])
for i in dll:
    cursor.execute(f'INSERT INTO {file_name} (name, type, cost, note) VALUES (?, ?, ?, ?)', (i[0], i[1], i[2], i[3]))




cursor.execute('''
''')

connection.commit()
connection.close()