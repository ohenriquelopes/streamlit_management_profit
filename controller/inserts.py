import sqlite3
conn = sqlite3.connect('my_data_base.db')
c = conn.cursor()

#############################

def add_userdata(username, password): #example
    c.execute('INSERT INTO userdata (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
