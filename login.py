import hashlib
import json
import os
import tkinter as tk
from tkinter import messagebox
from main import abre
<<<<<<< HEAD
import keyboard

=======
>>>>>>> 8359f42254e520c76ba2ce6d408d8411a39cfa06

def save_login(nome, senha):
    hashed_password = hashlib.sha256(senha.encode()).hexdigest()
    data = {}
<<<<<<< HEAD
    data_path = os.path.join(os.path.dirname(__file__), 'data.json')
    if os.path.exists(data_path):
        with open(data_path, 'r') as file:
            data = json.load(file)
    data[nome] = hashed_password
    with open(data_path, 'w', encoding='utf-8') as file:
=======
    if os.path.exists('C:/Users/marco/Desktop/v_horario/data.json'):
        with open('C:/Users/marco/Desktop/v_horario/data.json', 'r') as file:
            data = json.load(file)
    data[nome] = hashed_password
    with open('C:/Users/marco/Desktop/v_horario/data.json', 'w', encoding='utf-8') as file:
>>>>>>> 8359f42254e520c76ba2ce6d408d8411a39cfa06
        json.dump(data, file)

def check_login(nome, senha):
    hashed_password = hashlib.sha256(senha.encode()).hexdigest()
<<<<<<< HEAD
    data_path = os.path.join(os.path.dirname(__file__), 'data.json')
    if os.path.exists(data_path):
        with open(data_path, 'r', encoding='utf8') as file:
            data = json.load(file)
            saved_password = data.get(nome)
            if saved_password == hashed_password:
                return True
            else:
                return False
=======
    with open('C:/Users/marco/Desktop/v_horario/data.json', 'r', encoding='utf8') as file:
        data = json.load(file)
        saved_password = data.get(nome)
        if saved_password == hashed_password:
            return True
        else:
            return False
>>>>>>> 8359f42254e520c76ba2ce6d408d8411a39cfa06

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
<<<<<<< HEAD
    
    def exibe():
        login_window.destroy()  # Fechar a janela de login
        abre()  # Chamar a função abre() do arquivo main.py
        
    
=======

>>>>>>> 8359f42254e520c76ba2ce6d408d8411a39cfa06
    def login():
        nome = entry_nome.get().strip()
        senha = entry_senha.get().strip()

        if check_login(nome, senha):
            messagebox.showinfo('MR-Systems', 'Login realizado com sucesso!')
<<<<<<< HEAD
            exibe()  # Abrir o sistema principal após o login
        else:
            messagebox.showwarning('MR-Systems', 'Nome de usuário ou senha incorretos.')
    icon2_path = os.path.join(os.path.dirname(__file__), 'icon2.ico')
    login_window = tk.Tk()
    login_window.iconbitmap(icon2_path)
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
=======
            root.destroy()  # Fechar a janela de login após o login
            abre()
        else:
            messagebox.showwarning('MR-Systems', 'Nome de usuário ou senha incorretos.')

    root = tk.Tk()
    root.iconbitmap('C:/Users/marco/Desktop/v_horario/icon2.ico')
    root.geometry("300x200")
    root.title("MR-Systems")

    label_nome = tk.Label(root, text="Nome de usuário:")
    label_nome.pack()

    entry_nome = tk.Entry(root)
    entry_nome.pack()

    label_senha = tk.Label(root, text="Senha:")
    label_senha.pack()

    entry_senha = tk.Entry(root, show="*")
    entry_senha.pack()

    button_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar)
    button_cadastrar.pack()

    button_login = tk.Button(root, text="Login", command=login)
    button_login.pack()

    root.mainloop()
>>>>>>> 8359f42254e520c76ba2ce6d408d8411a39cfa06

screen()








<<<<<<< HEAD








=======
>>>>>>> 8359f42254e520c76ba2ce6d408d8411a39cfa06
