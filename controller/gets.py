import sqlite3
import datetime
import controller.select as s


def get_contas_fixas(conn):
    st.write("# Contas Fixas")
    results = s.select_all_contas_fixas()
    df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
    df.set_index(df.columns[0], inplace=True)
    st.dataframe(df)


def get_salarios_history():
    st.write("# Salários History")
    cursor.execute('SELECT * FROM salarios_history')
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
    df.set_index(df.columns[0], inplace=True)

    st.dataframe(df)

def get_soma_por_mes():
    st.write("# Salários History")
    cursor.execute('SELECT * FROM salarios_history')
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
    df.set_index(df.columns[0], inplace=True)

    soma_por_mes = df.groupby(df['mes_ano'])['entrada'].sum()
    st.dataframe(soma_por_mes)


def get_equivalente():
    st.write("# Equivalente")
    cursor.execute('SELECT * FROM rateio')
    results = cursor.fetchall()
    # pegar a entrada do mes (somada), e divir pelas % da tabela rateio
    df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
    df.set_index(df.columns[0], inplace=True)
    st.dataframe(df)




def get_rateio_mes():
    r1 = s.select_all_rateio()
    r2 = s.select_all_salario_history()
    df = pd.DataFrame(r2)
    df1 = pd.DataFrame(r1)
    soma = df.groupby(df[1])[2].sum()
    valor = soma.iloc[0]
    df1['resultado'] = valor * (df1[2] / 100)
    df1.set_index(df1.columns[0], inplace=True)
    df1 = df1.rename_axis('id')
    df1.columns = ['tag', 'porcentagem', 'resultado']
    valor = '{:,.2f}'.format(valor).replace(',', '|').replace('.', ',').replace('|', '.')
    df1['resultado'] = df1['resultado'].apply(
        lambda x: '{:,.2f}'.format(x).replace(',', '|').replace('.', ',').replace('|', '.')
    )
    st.text(valor)
    st.dataframe(df1)

def get_mes_atual():
    data_atual = datetime.datetime.now()
    mes_atual = data_atual.month
    st.write(mes_atual)


import sqlite3
import streamlit as st
import pandas as pd
import datetime
import controller.select as s

def get_contas_fixas(conn):
    st.write("# Contas Fixas")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contas_fixas')
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
    df.set_index(df.columns[0], inplace=True)
    st.dataframe(df)

def get_salarios_history(conn):
    st.write("# Salários History")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM salarios_history')
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
    df.set_index(df.columns[0], inplace=True)
    st.dataframe(df)

# Adicione as modificações necessárias nas outras funções semelhantes



