import pandas as pd
import re
from datetime import datetime, timedelta
import schedule
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import tkinter as tk
from tkinter import filedialog
from time import sleep
from tkinter import messagebox
import sys

   
def abre():
    vencendo_2h = []
    vencendo_atualizada = []
    icon2_path = os.path.join(os.path.dirname(__file__), 'icon2.ico')

    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(icon2_path)
    root.geometry('600x600+400+50')
    
    
    # Abre uma janela de diálogo para o usuário escolher o arquivo
    mensagem = messagebox.askyesno('MR-TEC', 'Selecione um arquivo em seu PC')
    if mensagem == True:
        file_path = filedialog.askopenfilename(title='MR-SOFTWARE', filetypes=[('Arquivos de texto','*.txt'), ('Arquivos csv', '*.csv')])
        if file_path == '':
            sys.exit()
    else:
        sys.exit()
    
    def msg_aguardar():    
        print('Aguarde enquanto o sistema está lendo o arquivo.')
    
    msg_aguardar()


    def Verifica_vencimento():
        
        codigos_4h = ['10', '50', '90', '110', '151', '365', '370', '1350', '1360', '1380', '1430',\
                    '1500', '1740', '1750', '1760', '1770', '1780', '1800', '1830', '1840', '2455',\
                    '2465', '3465']

        table = []
        vencendo_hoje = []
        padrao = r'\d{2}\.\d{2}'
        padrao_h_protocolo = r"(\.\d{4}\.)"
        filtrados = []
        
        with open(file_path, 'r', encoding='utf-8') as f:
            tabela = f.readlines()
            
        for linha in tabela:
            linha = str(linha).strip().split()
            table.append(linha)
        
        for linha in table:
            for l in linha:
                if l in codigos_4h:
                    vencendo_hoje.append(' '.join(linha))
                            
        for linha in vencendo_hoje:
            filtrado = linha
            
        df = pd.DataFrame(vencendo_hoje, columns=['coluna'])
        
       
        data_hoje = datetime.now().strftime('%d.%m')

        # Verifica se a data do protocolo é a mesma data do sistema
        for linha in df['coluna']:
            data_vencimento = linha[-5:]
            if data_vencimento == data_hoje:
                filtrados.append(linha)
                
        
        def cod_4h2():
            duas_horas = timedelta(hours=2)
            zero_hora = timedelta(hours=0)
            hora_agora = datetime.now().strftime('%H%M')
            hora_agora = datetime.strptime(hora_agora, '%H%M')
            for word in filtrados:
                hora_protocolo = re.search(padrao_h_protocolo, word).group()[1:-1]
                hora_protocolo = datetime.strptime(str(hora_protocolo), '%H%M')
                dif = hora_agora - hora_protocolo
            
                if dif >= duas_horas and dif > zero_hora and word not in vencendo_2h:
                    if len(vencendo_2h) < 1:
                        os.system('cls')
                    vencendo_2h.append(word)
                
                                
        cod_4h2()        
                    
    def atualiza():
        for l in vencendo_2h:
            if l not in vencendo_atualizada:
                sleep(2)
                alarme1()
                sleep(1)
                alarme2()
                vencendo_atualizada.append(l)
                print(f'{"---"*40} \n {vencendo_atualizada[-1:]}')
                
                
    def alarme1():
        som1_path= os.path.join(os.path.dirname(__file__),'notification_sounds', 'som1.mp3')
        pygame.init()
        pygame.mixer.music.load(som1_path)
        pygame.mixer.music.play()
        
                
    def alarme2():
        som2_path = os.path.join(os.path.dirname(__file__), 'notification_sounds', 'som2.mp3')
        pygame.init()
        pygame.mixer.music.load(som2_path)
        pygame.mixer.music.play()            

    def abrir_janela():
        janela = tk.Tk()
        text_box = tk.Text(janela)
        text_box.insert(tk.END, vencendo_atualizada)
        text_box.pack()
        janela.mainloop()
        return janela

    def job():
        Verifica_vencimento()
        atualiza()
        
                
        if len(vencendo_atualizada) < 1:
            os.system('cls')
            print(f'Ainda não há serviços vencendo nas próximas duas horas, estou atento verifiquei as {hora_agora} >>>')
            print('\nPressione (s) para sair')
            sleep(60)
   
    def on_key_press(event):
        if event.name == 's':
            if messagebox.askokcancel('Cancelar', 'Deseja fechar o sistema?'):
                os.abort()
    schedule.every(5).seconds.do(job)
    
    
    while True:
        schedule.run_pending()
        time.sleep(2)
        hora_agora = datetime.now().strftime('%H:%M')

print('Pressione (s) para sair')   



               
              
           
        
        
                
           
            

                

                             

    
               
        
             


           
                       
            
                    
                    
            

    





               
              
           
        
        
                
           
            

                

                             

    
               
        
             


           
                       
            
                    
                    
            

    




