import streamlit as st
import pandas as pd
import sqlite3
import datetime
conn = sqlite3.connect('my_data_base.db')
cursor = conn.cursor()

#############################

def create_table_rateio():
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

def create_table_contas_fixas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contas_fixas (
            id INTEGER PRIMARY KEY,
            mes_ano DATE,
            Luz NUMERIC,
            Agua NUMERIC,
            Aluguel NUMERIC,
            Spotify NUMERIC,
            Faculdade NUMERIC
        )
    ''')
    conn.commit()

def create_table_salarios_history():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS salarios_history (
            id INTEGER PRIMARY KEY,
            mes_ano DATE,
            entrada NUMERIC
        )
    ''')
    conn.commit()



