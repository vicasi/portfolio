from lib2to3.pytree import convert
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
import math
from types import NoneType

minha_janela = tk.Tk()
minha_entrada = tk.Entry()

def submit():
    print(minha_entrada.get())
minha_label = tk.Label(
    text="faça suas contas \o/",
    background='white',
    foreground='purple',
    font=("Verdana", 25)

)

def padrao_sinal(texto):
    padrao_sinal = r"\+|\-|\/|\*|\*\*|sqrt|x|X"
    regex_sinal = re.search(padrao_sinal, texto).group()
    return regex_sinal



def calculo():
    texto = minha_entrada.get()
    padrao_num0 = r"^\s*\d+\s*"
    padrao_num1 = r"\s*\d+\s*$"
    convert0 = int(re.search(padrao_num0, texto).group())
    regex1 = re.search(padrao_num1, texto)
    if regex1:        
        convert1 = int(regex1.group())
    sinal = padrao_sinal(texto)
    if sinal == '*' or sinal == 'x' or sinal == 'X':
        resultado = convert0 * convert1
        return resultado
    elif sinal == '/':
        resultado = convert0 / convert1
        return resultado
    elif sinal == '-':
        resultado = convert0 - convert1
        return resultado
    elif sinal == "+":
        resultado = convert0 + convert1
        return resultado
    elif sinal == '**':
        resultado = math.pow(convert0, convert1)
        return resultado
    elif sinal == 'sqrt':
        resultado = math.sqrt(convert0)
        return resultado
    else:
        return 'valor nao encontrado'


def resultado():
    messagebox.showinfo('resultado',calculo())

meu_botao2 = tk.Button(text='resultado',command=resultado)

#packs
minha_label.pack()
minha_entrada.pack()
meu_botao2.pack()










#loop
minha_janela.mainloop()