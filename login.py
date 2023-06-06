import hashlib
import json
import os
import tkinter as tk
from tkinter import messagebox
from rules import abre

def save_login(nome, senha):
    hashed_password = hashlib.sha256(senha.encode()).hexdigest()
    data = {}
    data_path = os.path.join(os.path.dirname(__file__), 'data.json')
    if os.path.exists(data_path):
        with open(data_path, 'r') as file:
            data = json.load(file)
    data[nome] = hashed_password
    with open(data_path, 'w', encoding='utf-8') as file:
        json.dump(data, file)

def check_login(nome, senha):
    hashed_password = hashlib.sha256(senha.encode()).hexdigest()
    data_path = os.path.join(os.path.dirname(__file__), 'data.json')
    if os.path.exists(data_path):
        with open(data_path, 'r', encoding='utf8') as file:
            data = json.load(file)
            saved_password = data.get(nome)
            if saved_password == hashed_password:
                return True
            else:
                return False

def screen():
    def cadastrar():
        nome = entry_nome.get().strip()
        senha = entry_senha.get().strip()

        if nome and senha:
            if check_login(nome, senha):
                messagebox.showwarning('MR-Systems', 'Usuário já cadastrado no sistema!')
            else:
                save_login(nome, senha)
                messagebox.showinfo('MR-Systems', 'Cadastro realizado com sucesso!')
        else:
            messagebox.showwarning('MR-Systems', 'Por favor, preencha todos os campos.')
    
    def exibe():
        login_window.destroy()  # Fechar a janela de login
        abre()  # Chamar a função abre() do arquivo main.py
        
    
    def login():
        nome = entry_nome.get().strip()
        senha = entry_senha.get().strip()

        if check_login(nome, senha):
            messagebox.showinfo('MR-Systems', 'Login realizado com sucesso!')
            exibe()  # Abrir o sistema principal após o login
        else:
            messagebox.showwarning('MR-Systems', 'Nome de usuário ou senha incorretos.')
    
    login_window = tk.Tk()
    login_window.iconbitmap('./icons/icon2.ico')
    login_window.geometry("300x200+480+200")
    login_window.title("MR-Systems")

    label_nome = tk.Label(login_window, text="Nome de usuário:")
    label_nome.pack()

    entry_nome = tk.Entry(login_window)
    entry_nome.pack()

    label_senha = tk.Label(login_window, text="Senha:")
    label_senha.pack()

    entry_senha = tk.Entry(login_window, show="*")
    entry_senha.pack()

    button_cadastrar = tk.Button(login_window, text="Cadastrar", command=cadastrar)
    button_cadastrar.pack()

    button_login = tk.Button(login_window, text="Login", command=login)
    button_login.pack()
    
    login_window.mainloop()


















