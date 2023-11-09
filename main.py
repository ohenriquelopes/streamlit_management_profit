import streamlit as st
import controller.gets as func_all


def main():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    st.markdown('<link rel="stylesheet" type="text/css" href="custom.css">', unsafe_allow_html=True)



    st.selectbox("Pick one", ["cats", "dogs"])


if __name__ == '__main__':
    main()

