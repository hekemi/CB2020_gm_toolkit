import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from data.database_metods import *

def names():
    names = os.listdir('data\characters')
    actual_name = []
    for i in names:
        actual_name.append(i[:-3])
    return actual_name
