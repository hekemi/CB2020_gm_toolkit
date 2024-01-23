import sqlite3
from database_metods import *
import json

# db = Database('data\characters\Fait.db')


data = extract_stats('Fait')
stat = show_stat(data, 'REF')
print(stat)


# db.disconnect()

# (data[data['name'] == 'REF'].values[0])[2]