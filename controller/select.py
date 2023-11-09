import sqlite3
conn = sqlite3.connect('my_data_base.db')
cursor = conn.cursor()

#############################


def select_all_rateio():
    cursor.execute('SELECT * FROM rateio')
    results = cursor.fetchall()
    return results
    # st.write(results)
def select_all_history():
    cursor.execute('SELECT * FROM salarios_history')
    results = cursor.fetchall()
    return results

def select_all_contas_fixas():
    cursor.execute('SELECT * FROM contas_fixas')
    results = cursor.fetchall()
    return results

