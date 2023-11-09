import streamlit as st
import pandas as pd
import sqlite3
import datetime

conn = sqlite3.connect('my_data_base.db')
cursor = conn.cursor()


def select_all_rateio():
    cursor.execute('SELECT * FROM rateio')
    results = cursor.fetchall()
    return results
    # st.write(results)
def select_all_history():
    cursor.execute('SELECT * FROM salarios_history')
    results = cursor.fetchall()
    return results