import streamlit as st
import pandas as pd
import sqlite3
import pages.func_all as func_all
import datetime


def main():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    st.markdown('<link rel="stylesheet" type="text/css" href="custom.css">', unsafe_allow_html=True)


    func_all.get_rateio_mes()
    func_all.get_mes_atual()



if __name__ == '__main__':
    main()

