import controller.connection as connection
import pandas as pd
import streamlit as st




def select_all_rateio():
    c = connection.connect()
    c.execute('SELECT * FROM rateio')
    results = c.fetchall()
    df = pd.DataFrame(results, columns=[desc[0] for desc in c.description])
    df.set_index(df.columns[0], inplace=True)
    st.dataframe(df)

def select_all_salario_history():
    c = connection.connect()
    c.execute('SELECT * FROM salarios_history')
    results = c.fetchall()
    df = pd.DataFrame(results, columns=[desc[0] for desc in c.description])
    df.set_index(df.columns[0], inplace=True)
    df['entrada'] = df['entrada'].apply(
        lambda x: '{:,.2f}'.format(x).replace(',', '-').replace('.', ',').replace('-', '.')
    )
    st.dataframe(df)


def select_grouped_salario_history():
    c = connection.connect()
    c.execute('SELECT * FROM salarios_history')
    results = c.fetchall()
    df = pd.DataFrame(results, columns=[desc[0] for desc in c.description])
    df.set_index(df.columns[0], inplace=True)
    soma_por_mes = df.groupby(df['mes_ano'])['entrada'].sum()
    # soma_por_mes.columns = ['mes_ano', 'entrada']
    # soma_por_mes['entrada'] = soma_por_mes['entrada'].apply(
    #     lambda x: '{:,.2f}'.format(x).replace(',', '-').replace('.', ',').replace('-', '.')
    # )
    st.dataframe(soma_por_mes)


def select_teste():
    c = connection.connect()
    c.execute('SELECT * FROM salarios_history')
    results = c.fetchall()
    df = pd.DataFrame(results, columns=[desc[0] for desc in c.description])
    df.set_index(df.columns[0], inplace=True)
    df.columns = ['mes_ano', 'entrada']
    # df['entrada'] = df['entrada'].apply(lambda x: '{:,.2f}'.format(x).replace(',', '-').replace('.', ',').replace('-', '.'))
    # soma_por_mes = df.groupby(df['mes_ano'])['entrada'].sum()
    # soma_por_mes['entrada'] = '{:,.2f}'.format(soma_por_mes.iloc[0]).replace(',', '-').replace('.', ',').replace('-', '.')
    df['entrada'] = df['entrada'].apply(
        lambda x: float(x.replace(',', '').replace('.', '').replace(',', '.')) if isinstance(x, str) else x)
    # df['mes_ano'] = pd.to_datetime(df['mes_ano'])  # Certifique-se de que 'mes_ano' é do tipo datetime
    # df.set_index('mes_ano', inplace=True)
    # soma_por_mes = df.groupby(df.index)['entrada'].sum()
    soma_por_mes = df.groupby('mes_ano')['entrada'].sum()

    soma_por_mes = soma_por_mes.apply(lambda x: '{:,.2f}'.format(x)).str.replace(',', '-').str.replace('.',',').str.replace('-', '.')

    st.dataframe(soma_por_mes)

    # st.write(soma_por_mes.iloc[0])
    # soma_por_mes.iloc[0] = soma_por_mes.iloc[0] + 9999
    # st.write(soma_por_mes.iloc[0])
    # st.dataframe(soma_por_mes)


def select_all_contas_fixas():
    c = connection.connect()
    c.execute('SELECT * FROM contas_fixas')
    results = c.fetchall()
    df = pd.DataFrame(results, columns=[desc[0] for desc in c.description])
    df.set_index(df.columns[0], inplace=True)
    st.dataframe(df)

