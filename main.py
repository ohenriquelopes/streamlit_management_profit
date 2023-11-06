import streamlit as st
import pandas as pd
import sqlite3
import pages.func_all as func_all


def main():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    st.markdown('<link rel="stylesheet" type="text/css" href="custom.css">', unsafe_allow_html=True)


    # func_all.get_contas_fixas()
    # func_all.get_salarios_history()
    # func_all.get_equivalente()
    #
    # func_all.get_soma_por_mes()

    # idk = func_all.get_soma_por_mes()
    # idk2 = func_all.get_equivalente()

    # func_all.get_equivalente_calculado()

    # idk2['resultado'] = idk['entrada'] * (idk2['Porcentagem'] / 100)
    # st.dataframe(idk2)

    # idk2 = func_all.calcular_e_adicionar_coluna(idk, idk2)
    # st.dataframe(idk2)

    # st.sidebar.header("Menu")
    # conn = sqlite3.connect('my_data_base.db')
    # cursor = conn.cursor()

    #
    # df = func_all.query_rateio()
    # st.write(df)
    # df1 = df
    # st.write(df1[0])
    # st.write(df1[0][2])
    func_all.get_div_mes()


if __name__ == '__main__':
    main()

