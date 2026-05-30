import streamlit as st
def header_home():
    # st.image("src/assets/images/home_logo.png", width=100)
    st.markdown("""
            <div style='display:flex;align-items:center;justify-content:center;flex-direction:column;margin-bottom:30px;margin-top:30px;'>
                <img src="https://i.ibb.co/YTYGn5qV/logo.png" style="height:100px;">
                <h1 style='text-align:center;color:#E0E3FF;'>Attend<br/>AI</h1>
            </div>
               """,unsafe_allow_html=True)              