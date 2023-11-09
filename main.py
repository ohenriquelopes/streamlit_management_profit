import streamlit as st
import controller.select as s


def main():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    st.markdown('<link rel="stylesheet" type="text/css" href="custom.css">', unsafe_allow_html=True)



    # st.selectbox("Pick one", ["cats", "dogs"])

    s.select_all_rateio()
    s.select_all_contas_fixas()
    s.select_all_salario_history()
    # s.select_grouped_salario_history()
    st.write('dauiedua')
    s.select_teste()


if __name__ == '__main__':
    main()

