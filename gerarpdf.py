
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.lib.units import cm
from reportlab.lib import colors
import os

print('ate aqui')

class gerar1():

    def gerar(self):
                #captura as entradas do usuario
        self.addnumer_leb = str(self.input_numero).upper()
        self.addnome_leb = self.input_nome.upper()
        self.addfun_leb = self.input_funcao.upper()
        self.addexped_leb = str(self.input_expedicao).upper()
        self.addval_leb = str(self.input_nascimento).upper()
        self.addRG_leb = self.input_rg.upper()
        self.addCPF_leb = self.input_cpf.upper()
        self.addcivil_leb = self.input_estadoCiv.upper()
        self.addbatism_leb = str(self.input_batismo).upper()
        self.addfiliacao_leb = self.input_filiacao1.upper()
        self.addfiliacao_2b = self.input_filiacao2.upper()
        print('entradas capturadas com sucessso')
                #gera e salva dados de entrada capturados 
        self.c = canvas.Canvas(f"./bd_credenciais/{self.addnumer_leb}.pdf")                               
        self.num_ficha = self.addnumer_leb
        self.nome_membro = self.addnome_leb
        self.func_cargo = self.addfun_leb
        self.data_exped = self.addexped_leb
        self.data_nasc = self.addval_leb
        self.rg_membro = self.addRG_leb
        self.cpf_membro = self.addCPF_leb
        self.estado_civ = self.addcivil_leb
        self.data_batismo = self.addbatism_leb
        self.mae_membro = self.addfiliacao_leb
        self.pai_membro = self.addfiliacao_2b   
                #fonte de texto    
        self.c.setFont("Helvetica", 8,)
                # metodo de escala da imagem de fundo        
        self.c.translate(cm,cm)
                #condições que indentifica função do membro e altera a credencial
        if self.func_cargo == 'MEMBRO':
            self.c.drawImage("Credencial2.png", 20, 635, width=500, height=165)
            self.c.hAlign = 'CENTER'
            self.c.drawString(159, 705, self.num_ficha)
            self.c.drawString(30, 685, self.nome_membro)
            self.c.drawString(30, 657, self.func_cargo)
            self.c.drawString(100, 657, self.data_exped)
            self.c.drawString(154, 657, self.data_nasc)
            self.c.drawString(308, 775, self.rg_membro)
            self.c.drawString(408, 775, self.cpf_membro)
            self.c.drawString(315, 746, self.estado_civ)
            self.c.drawString(413, 746, self.data_batismo)
            self.c.drawString(300, 714, self.mae_membro)
            self.c.drawString(300, 702, self.pai_membro)
        elif self.func_cargo == 'DIACONO':
            self.c.drawImage("Credencial3.png", 20, 635, width=500, height=165)
            self.c.hAlign = 'CENTER'
            self.c.drawString(159, 705, self.num_ficha)
            self.c.drawString(30, 685, self.nome_membro)
            self.c.drawString(30, 657, self.func_cargo)
            self.c.drawString(100, 657, self.data_exped)
            self.c.drawString(154, 657, self.data_nasc)
            self.c.drawString(308, 775, self.rg_membro)
            self.c.drawString(408, 775, self.cpf_membro)
            self.c.drawString(315, 746, self.estado_civ)
            self.c.drawString(413, 746, self.data_batismo)
            self.c.drawString(300, 714, self.mae_membro)
            self.c.drawString(300, 702, self.pai_membro)
        elif self.func_cargo == 'PRESBíTERO':
            self.c.drawImage("Credencial3.png", 20, 635, width=500, height=165)
            self.c.hAlign = 'CENTER'
            self.c.drawString(159, 705, self.num_ficha)
            self.c.drawString(30, 685, self.nome_membro)
            self.c.drawString(30, 657, self.func_cargo)
            self.c.drawString(100, 657, self.data_exped)
            self.c.drawString(154, 657, self.data_nasc)
            self.c.drawString(308, 775, self.rg_membro)
            self.c.drawString(408, 775, self.cpf_membro)
            self.c.drawString(315, 746, self.estado_civ)
            self.c.drawString(413, 746, self.data_batismo)
            self.c.drawString(300, 714, self.mae_membro)
            self.c.drawString(300, 702, self.pai_membro)
        elif self.func_cargo == 'EVANGELISTA':
            self.c.drawImage("Credencial3.png", 20, 635, width=500, height=165)
            self.c.hAlign = 'CENTER'
            self.c.drawString(159, 705, self.num_ficha)
            self.c.drawString(30, 685, self.nome_membro)
            self.c.drawString(30, 657, self.func_cargo)
            self.c.drawString(100, 657, self.data_exped)
            self.c.drawString(154, 657, self.data_nasc)
            self.c.drawString(308, 775, self.rg_membro)
            self.c.drawString(408, 775, self.cpf_membro)
            self.c.drawString(315, 746, self.estado_civ)
            self.c.drawString(413, 746, self.data_batismo)
            self.c.drawString(300, 714, self.mae_membro)
            self.c.drawString(300, 702, self.pai_membro)
        elif self.func_cargo == 'PASTOR':
            self.c.drawImage("Credencial4.png", 20, 635, width=500, height=165)
            self.c.hAlign = 'CENTER'
            self.c.drawString(30, 657, self.num_ficha)
            self.c.drawString(30, 685, self.nome_membro)
            self.c.drawString(100, 657, self.data_exped)
            self.c.drawString(154, 657, self.data_nasc)
            self.c.drawString(308, 775, self.rg_membro)
            self.c.drawString(408, 775, self.cpf_membro)
            self.c.drawString(315, 746, self.estado_civ)
            self.c.drawString(413, 746, self.data_batismo)
            self.c.drawString(300, 714, self.mae_membro)
            self.c.drawString(300, 702, self.pai_membro)
            
        self.c.showPage()
        self.c.save()
        print('credencial gerada com sucesso até o final')

    

    

    
#gerar1()
        




