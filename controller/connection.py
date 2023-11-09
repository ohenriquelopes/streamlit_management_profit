import sqlite3


#############################

def connect():
    conn = sqlite3.connect('my_data_base.db')
    c = conn.cursor()
    return c

