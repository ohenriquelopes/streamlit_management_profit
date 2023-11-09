import streamlit as st
import pandas as pd
import sqlite3




st.set_page_config(page_title="Plotting Demo", page_icon="📈")

# st.markdown("# Plotting Demo")
# st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

# Conectar ao banco de dados (ou criar um novo se não existir)
conn = sqlite3.connect('my_data_base.db')

# Criar um cursor
cursor = conn.cursor()



# Executar a consulta para criar a tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contas_fixas (
        id INTEGER PRIMARY KEY,
        mes_ano TEXT,
        Luz NUMERIC,
        Agua NUMERIC,
        Aluguel NUMERIC,
        Spotify NUMERIC,
        Faculdade NUMERIC
    )
''')

# Commit para salvar as alterações no banco de dados
# conn.commit()
#
# cursor.execute('''
#     INSERT INTO contas_fixas (mes_ano, Luz, Agua, Aluguel, Spotify, Faculdade)
#     VALUES ('2021-01', 100, 50, 500, 30, 100)
# ''')

conn.commit()
# Fechar a conexão com o banco de dados
conn.close()
