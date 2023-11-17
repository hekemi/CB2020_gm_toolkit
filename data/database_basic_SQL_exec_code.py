import sqlite3
import database_metods as db_m


db_m.create_new_character('Sadam_Huseyn')

connection = sqlite3.connect('data\Motherbase.db')
cursor = connection.cursor()

cursor.execute('''

''')

connection.commit()
connection.close()