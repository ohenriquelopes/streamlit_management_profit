import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('my_data_base.db')
cursor = conn.cursor()


def get_contas_fixas():
    st.write("# Contas Fixas")
    cursor.execute('SELECT * FROM contas_fixas')
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
    df.set_index(df.columns[0], inplace=True)
    st.dataframe(df)


def get_salarios_history():
    st.write("# Salários History")
    cursor.execute('SELECT * FROM salarios_history')
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
    df.set_index(df.columns[0], inplace=True)
    # df['entrada'] = df['entrada'].apply(
    #     lambda x: '{:,.2f}'.format(x)
        # .replace(',', '|').replace('.', ',').replace('|', '.'))
    st.dataframe(df)

def get_soma_por_mes():
    st.write("# Salários History")
    cursor.execute('SELECT * FROM salarios_history')
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
    df.set_index(df.columns[0], inplace=True)
    # df['entrada'] = df['entrada'].apply(
    #     lambda x: '{:,.2f}'.format(x)
        # .replace(',', '|').replace('.', ',').replace('|', '.'))
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


def query_rateio():
    cursor.execute('SELECT * FROM rateio')
    results = cursor.fetchall()
    return results
    # st.write(results)
def query_salarios_history():
    cursor.execute('SELECT * FROM salarios_history')
    results = cursor.fetchall()
    return results

def get_rateio_mes():
    r1 = query_rateio()
    r2 = query_salarios_history()
    df = pd.DataFrame(r2)
    df1 = pd.DataFrame(r1)
    soma = df.groupby(df[1])[2].sum()
    valor = soma.iloc[0]
    df1['resultado'] = valor / df1[2]
    df1.set_index(df1.columns[0], inplace=True)
    # Renomeie a coluna de índice para 'novo_indice'
    df1 = df.rename_axis('id')
    df1.columns = ['tag', 'porcentagem', 'resultado']
    valor = '{:,.2f}'.format(valor).replace(',', '|').replace('.', ',').replace('|', '.')
    st.text(valor)
    st.dataframe(df1)


def calcular_e_adicionar_coluna(df1, df2):
    df2['resultado'] = df1 * (df2['Porcentagem'] / 100)
    return df2


def get_equivalente_calculado():
    st.write("# Equivalente Calculado")
    result1 = query_rateio()
    # pegar a entrada do mes (somada), e divir pelas % da tabela rateio
    df = pd.DataFrame(result1, columns=[desc[0] for desc in cursor.description])
    df.set_index(df.columns[0], inplace=True)
    ###############

    result2 = query_salarios_history()
    df1 = pd.DataFrame(result2, columns=[desc[0] for desc in cursor.description])
    df1.set_index(df.columns[0], inplace=True)
    # df['entrada'] = df['entrada'].apply(
    #     lambda x: '{:,.2f}'.format(x)
        # .replace(',', '|').replace('.', ',').replace('|', '.'))
    # soma_por_mes = df1.groupby(df1['mes_ano'])['entrada'].sum()
    ###############

    # df['resultado'] = soma_por_mes['entrada'] * (df['Porcentagem'] / 100)

    st.dataframe(df)
    st.dataframe(df1)

