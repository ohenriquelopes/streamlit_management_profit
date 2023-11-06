import streamlit as st
import pandas as pd
import sqlite3


conn = sqlite3.connect('my_data_base.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS rateio (
        id INTEGER PRIMARY KEY,
        Tag TEXT,
        Porcentagem NUMERIC
    )
''')

cursor.execute('''
    INSERT INTO rateio (Tag, Porcentagem)
    SELECT 'Investimento', 30
    WHERE NOT EXISTS (SELECT 1 FROM rateio)
    UNION ALL
    SELECT 'Contas-fixas', 50
    WHERE NOT EXISTS (SELECT 1 FROM rateio)
    UNION ALL
    SELECT 'Lazer', 10
    WHERE NOT EXISTS (SELECT 1 FROM rateio)
    UNION ALL
    SELECT 'Outros', 10
    WHERE NOT EXISTS (SELECT 1 FROM rateio) 
''')



conn.commit()
conn.close()