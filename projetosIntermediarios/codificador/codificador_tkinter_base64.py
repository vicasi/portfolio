from cProfile import label
import tkinter as tk
from tkinter import ttk
import base64
from typing import final


def decodificador(text):
    b_text = text.encode('ascii')
    b64_text = base64.b64encode(b_text)
    final_text = b64_text.decode('ascii')
    print(final_text)
    b_final_text = final_text.encode('ascii')
    b64_text = base64.b64decode(b_final_text)
    b64_text = b64_text.decode('ascii')
    return [final_text, b64_text]

def app():

    def submit(event):
        decodified_text = decodificador(text_entry.get())
        original_label = tk.Label(text=f'a original: {decodified_text[1]}')
        codified_label = tk.Label(text=f'a codificada: {decodified_text[0]}')
        codified_label.grid(sticky=tk.S)
        original_label.grid(sticky=tk.S)



    root = tk.Tk()
    largura_janela = 900
    altura_janela = 600
    altura_tela = root.winfo_screenheight()
    y = int(altura_tela/2 - altura_janela / 2)
    root.geometry(f'{largura_janela}x{altura_janela}+{300}+{y}')
    instrucoes = tk.Label(text='simplesmente digite e aperte tab em seguida enter ou click no botao para receber seu texto codificado')
    instrucoes.grid(sticky=tk.N)
    text_entry = tk.StringVar()
    entry = ttk.Entry(root, textvariable=text_entry)
    entry.grid(sticky=tk.N)
    button = tk.Button(root, text='pressione enter')
    button.bind('<Return>', submit)
    button.focus()
    button.grid(sticky=tk.W)








    root.mainloop()
























if __name__ == '__main__':
    app()