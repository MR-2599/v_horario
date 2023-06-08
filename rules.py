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
class Vencimentos:
    def __init__(self):
        pass
    def abre(self):
        self.vencendo_2h = []
        self.vencendo_atualizada = []
        

        root = tk.Tk()
        root.withdraw()
        root.iconbitmap('./icons/icon2.ico')
        root.geometry('600x600+400+50')
        
        
        # Abre uma janela de para o usuário o local do arquivo
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

        def verifica_vencimento(self):
            
            self.codigos_4h = ['10', '50', '90', '110', '151', '365', '370', '1350', '1360', '1380', '1430',\
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
                    if l in self.codigos_4h:
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
                    
            
            def cod_4h2(self):
                self.duas_horas = timedelta(hours=2)
                self.zero_hora = timedelta(hours=0)
                self.hora_agora = datetime.now().strftime('%H%M')
                self.hora_agora = datetime.strptime(self.hora_agora, '%H%M')
                for word in filtrados:
                    self.hora_protocolo = re.search(padrao_h_protocolo, word).group()[1:-1]
                    self.hora_protocolo = datetime.strptime(str(self.hora_protocolo), '%H%M')
                    self.dif = self.hora_agora - self.hora_protocolo
                
                    if self.dif >= self.duas_horas and self.dif > self.zero_hora and word not in self.vencendo_2h:
                        if len(self.vencendo_2h) < 1:
                            os.system('cls')
                        self.vencendo_2h.append(word)
                    
                                    
            cod_4h2(self)        
                        
        def atualiza(self):
            for l in self.vencendo_2h:
                if l not in self.vencendo_atualizada:
                    sleep(2)
                    alarme1()
                    sleep(1)
                    alarme2()
                    self.vencendo_atualizada.append(l)
                    print(f'{"---"*40} \n {self.vencendo_atualizada[-1:]}')
                    
                    
        def alarme1():
            som1_path = './notification_sounds/som1.mp3'
            pygame.init()
            pygame.mixer.music.load(som1_path)
            pygame.mixer.music.play()
            
                    
        def alarme2():
            som2_path = './notification_sounds/som2.mp3'
            pygame.init()
            pygame.mixer.music.load(som2_path)
            pygame.mixer.music.play()            

        def abrir_janela():
            janela = tk.Tk()
            text_box = tk.Text(janela)
            text_box.insert(tk.END, self.vencendo_atualizada)
            text_box.pack()
            text_box.iconbitmap('./icons/icon2.ico')
            janela.mainloop()
            return janela

        def job():
            verifica_vencimento(self)
            atualiza(self)
            
                    
            if len(self.vencendo_atualizada) < 1:
                os.system('cls')
                print(f'Ainda não há serviços vencendo nas próximas duas horas, estou atento verifiquei as {hora_agora} >>>')
                print('\nPressione (s) para sair')
                sleep(60)
    
        
        schedule.every(5).seconds.do(job)
        
        
        while True:
            schedule.run_pending()
            time.sleep(2)
            hora_agora = datetime.now().strftime('%H:%M')

   



               
              
           
        
        
                
           
            

                

                             

    
               
        
             


           
                       
            
                    
                    
            

    





               
              
           
        
        
                
           
            

                

                             

    
               
        
             


           
                       
            
                    
                    
            

    




