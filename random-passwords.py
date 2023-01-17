import tkinter as tk
from tkinter import *
from random import choice
import string

qntnumeros = ['10 digitos', '15 digitos', '20 digitos', '69 digitos', '666 digitos']

janela = Tk()
janela.title('Gerador de senha')
janela.geometry('240x130')

class Popup:

    def __init__(self, title:str="Popup", message:str="", master=None):

        if master is None:
            master = tk._get_default_root()

        self.root = tk.Toplevel(master)

        self.root.minsize(250, 40)

        self.root.resizable(False, False)

        self.root.protocol("WM_DELETE_WINDOW", self.destroy)

        self.root.title(title)

        width = max(map(len, message.split("\n")))
        height = message.count("\n") + 1

        self.text = tk.Text(self.root, bg="#f0f0ed", height=height,
                            width=width, highlightthickness=0, bd=0,
                            selectbackground="orange")

        self.text.insert("end", message)

        self.text.config(state="disabled")
        self.text.pack()

        self.button = tk.Button(self.root, text="Ok", command=self.destroy)
        self.button.pack()

        self.root.grab_set()

        self.root.mainloop()

    def destroy(self) -> None:

        self.root.quit()
        self.root.destroy()

def var_states():

    if clicked_qnt.get() == '10 digitos':

        tamanho_da_senha = 10
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha_segura = ''

        for i in range(tamanho_da_senha):
            senha_segura += choice(caracteres)

        Popup(title="sua nova senha", message=senha_segura, master=janela)

    if clicked_qnt.get() == '15 digitos':

        tamanho_da_senha = 15
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha_segura = ''

        for i in range(tamanho_da_senha):
            senha_segura += choice(caracteres)

        Popup(title="sua nova senha", message=senha_segura, master=janela)

    if clicked_qnt.get() == '69 digitos':

        tamanho_da_senha = 69
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha_segura = ''

        for i in range(tamanho_da_senha):
            senha_segura += choice(caracteres)

        Popup(title="sua nova senha", message=senha_segura, master=janela)

    if clicked_qnt.get() == '20 digitos':

        tamanho_da_senha = 20
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha_segura = ''

        for i in range(tamanho_da_senha):
            senha_segura += choice(caracteres)

        Popup(title="sua nova senha", message=senha_segura, master=janela)

    if clicked_qnt.get() == '667 digitos':

        tamanho_da_senha = 667
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha_segura = ''

        for i in range(tamanho_da_senha):
            senha_segura += choice(caracteres)

        Popup(title="Sua nova senha", message=senha_segura, master=janela)


Label(janela, text="").grid(row=5, sticky=W)
clicked_qnt = StringVar()
clicked_qnt.set('Quantidade de digitos na senha')

dropmenu = OptionMenu(janela, clicked_qnt, *qntnumeros).grid(row=5, sticky=E, pady=20)


Button(janela, text='Iniciar', command=var_states).grid(row=7, sticky=N, pady=9)
janela.mainloop()