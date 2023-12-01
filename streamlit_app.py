# streamlit_app.py

import streamlit as st
from app_main import app_class
from time import sleep

#script de login
#script main
def check_password():
            def widget_tela_login():
                        titulo_login = st.title('Ass de Deus :orange[_Monte Sinai_]')
                        st.subheader(' :blue[_Uma Revelação de Deus_]')
                        st.divider()
                        st.subheader('Faça seu Login')   
            
                #Retorna `True` se o usuário tiver uma senha correta.
            
            def password_entered():
                
                
                #Verifica se a senha digitada pelo usuário está correta.
                if (
                    st.session_state["username"] in st.secrets["passwords"]
                    and st.session_state["password"]
                    == st.secrets["passwords"][st.session_state["username"]]
                ):
                    st.session_state["password_correct"] = True
                    del st.session_state["password"]  # não armazene nome de usuário + senha
            
                    #del st.session_state["username"]
                    
                    
                else:
                    st.session_state["password_correct"] = False
            
            if "password_correct" not in st.session_state:
                widget_tela_login()
                
                
                # Primeira execução, mostre as entradas para nome de usuário + senha.
                st.text_input("Usuário", on_change=password_entered, key="username")
                st.text_input(
                    "Senha", type="password", on_change=password_entered, key="password"
                )
            
                
            
            elif not st.session_state["password_correct"]:
                widget_tela_login()
                # Password not correct, show input + error.
                st.text_input("Username", on_change=password_entered, key="username")
                st.text_input(
                    "Password", type="password", on_change=password_entered, key="password"
                )
                st.error("😕 Usuário desconhecido ou senha incorreta")
                return False
            else:
                # Password correct.
                return True


    
if check_password():
    app_class()
  
    
    
