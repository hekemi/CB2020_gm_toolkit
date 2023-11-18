import sqlite3
import database_metods as db_m

connection = sqlite3.connect('data\Motherbase.db')
cursor = connection.cursor()

cursor.execute('''

''')

connection.commit()
connection.close()