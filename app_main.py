#documentação:https://docs.streamlit.io/library/api-reference/widgets/st.number_input
import streamlit as st;
from datetime import date
import time
import datetime
import os
from gerarpdf import gerar1

from fpdf import FPDF


class app_class():

    def __init__(self):
        self.usuario = 'indefinido'
        data = date.today()
        print(f'O Usuario {self.usuario} fez login as {data}')
        
                #menu lateral - sidebar
        self.menuPrincipal = st.sidebar.title('Menu Principal')
        self.menuPrincipal = st.sidebar.selectbox("Escolha uma Pagina",("Inicio", "Emitir Credencial", "Vendas", "Calcular Material"))
                
                #Pg inicial e widgets
        if self.menuPrincipal == 'Inicio':            
                #Informações do Topo da pagina
            titulo_Igreja = st.title('Ass de Deus :orange[_Monte Sinai_]')
            st.subheader(' :blue[_Uma Revelação de Deus_]')
            st.divider()
            st.subheader('Administração COEMADMS')
            texte_info = st.text(f"""USER:{self.usuario} | COD:007-01 | {data}
FUNC:Secretario""")
            st.caption('Para sua segurança seu login foi salvo no historico.')
            st.caption("""_Se o seu dom é servir, sirva; se é ensinar, ensine;
Romanos 12:7_""")

                #seleções do menu lateral
        if self.menuPrincipal == 'Emitir Credencial':
            self.tela_emitir_credencial()

        if self.menuPrincipal == 'Produtos':
            pass
        
            

    def tela_emitir_credencial(self): #Pg Emissão de Credenciais
        data = date.today()
        """titulo_Igreja = st.title("Ass de Deus :orange[_Monte Sinai_]")
        st.subheader(' :blue[_Uma Revelação de Deus_]')
        st.divider()"""  # 👈 Draws a horizontal rule
        st.subheader('Emitir Credenciais')
        texte_info = st.text(f'USER:{self.usuario} | COD:007-01 | {data}')
        st.caption('Para sua segurança seu login foi salvo no historico.')
        st.caption('_Sempre Revise com :red[Atenção] antes de salvar._')        
                    #entradas
        self.input_numero = st.text_input('Numero da Ficha')
        self.input_nome = st.text_input('Nome')
        self.input_funcao = st.selectbox(
    'Função',
    ('', 'Membro', 'Diácono', 'Prebítero', 'Evangelista', 'Pastor'))
        self.input_expedicao = st.date_input("Expedição",  (datetime.date.today()), format="DD/MM/YYYY")
        self.input_nascimento = st.date_input("Nascimento", (datetime.date.today()), format="DD/MM/YYYY")
        self.input_rg = st.text_input('RG')
        self.input_cpf = st.text_input('Cpf')
        self.input_estadoCiv = st.selectbox(
    'Estado Civil',
    ('', 'Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)'))        
        self.input_batismo = st.date_input("Data de Batismo", (datetime.date.today()), format="DD/MM/YYYY")
        self.input_filiacao1 = st.text_input('Filiação(Mãe)')
        self.input_filiacao2 = st.text_input('Filiação (Pai)')
        
        if st.button('Salvar'):
            st.write('Salvo com Sucesso!')
            gerar1.gerar(self)
            with open(f"./bd_credenciais/{self.input_numero}.pdf", "rb") as f:
                st.download_button(f"Download Credencial", f, f"{self.input_numero}.pdf")

        if st.button('Limpar'):
            st.write('Não foi salvo ainda')
            
            
        else:
            st.write('Não foi salvo ainda')
        
        
        
        

#app_class()
