# streamlit_app.py
import hmac
import streamlit as st
from app_main import app_class
import os
import datetime
from time import sleep

def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            titulo_login = st.title('Ass de Deus :orange[_Monte Sinai_]')
            st.subheader(' :blue[_Uma Revelação de Deus_]')
            st.divider()
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            user_loog = str(st.session_state["username"])
            st.session_state["password_correct"] = True
            arquivo = open('user_log.txt', 'r+')
            print(arquivo.readlines()) #Consegue ler
            arquivo.write(f'{user_loog}' +"\n") #consegue editar
            arquivo.close()
            
            del st.session_state["password"]  # Don't store the username or password.
            #del st.session_state["username"]
            
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if check_password():
    #st.write(st.session_state["username"])    
    app_class()
