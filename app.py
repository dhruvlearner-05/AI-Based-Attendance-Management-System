# import streamlit as st
# def main():
#     st.title("Hello, Streamlit!")
#     st.write("This is a simple Streamlit app.")
#     name=st.text_input("Enter your name:")
#     col1,col2=st.columns(2)
#     with col1:
#         if(st.button("display by name",type="primary",key="btn1",width="stretch")):
#             st.write(f"Hello, {name}!")
#     with col2:
#         if(st.button("display by name",type="secondary",key="btn2",width="stretch")):
#             st.write(f"Welcome, {name}!")
#     st.markdown("# This is a markdown text.")
#     st.markdown("""
#                 <style>
#                     button{
#                         background:green !important;
#                     }
#                 </style>"""
#                 ,unsafe_allow_html=True)
# main()
import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
def main():
    if "login_type" not in st.session_state:
        st.session_state["login_type"]=None
    match st.session_state["login_type"]:
        case "teacher":
            teacher_screen()
        case "student":
            student_screen()
        case None:
            home_screen()
main()