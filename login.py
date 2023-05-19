import hashlib
import json
import os
import tkinter as tk
from tkinter import messagebox
from main import abre

def save_login(nome, senha):
    hashed_password = hashlib.sha256(senha.encode()).hexdigest()
    data = {}
    if os.path.exists('data.json'):
        with open('data.json', 'r') as file:
            data = json.load(file)
    data[nome] = hashed_password
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)

def check_login(nome, senha):
    hashed_password = hashlib.sha256(senha.encode()).hexdigest()
    with open('data.json', 'r', encoding='utf8') as file:
        data = json.load(file)
        saved_password = data.get(nome)
        if saved_password == hashed_password:
            return True
        else:
            return False

def screen():
    def cadastrar():
        nome = entry_nome.get().strip().capitalize()
        senha = entry_senha.get().strip()

        if nome and senha:
            if check_login(nome, senha):
                messagebox.showwarning('MR-Systems', 'Usuário já cadastrado no sistema!')
            else:
                save_login(nome, senha)
                messagebox.showinfo('MR-Systems', 'Cadastro realizado com sucesso!')
        else:
            messagebox.showwarning('MR-Systems', 'Por favor, preencha todos os campos.')

    def login():
        nome = entry_nome.get().strip().capitalize()
        senha = entry_senha.get().strip()

        if check_login(nome, senha):
            messagebox.showinfo('MR-Systems', 'Login realizado com sucesso!')
            root.destroy()  # Fechar a janela de login após o login
            abre()
        else:
            messagebox.showwarning('MR-Systems', 'Nome de usuário ou senha incorretos.')

    root = tk.Tk()
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

screen()








