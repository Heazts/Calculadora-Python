import tkinter as tk
from tkinter import ttk
import ttkthemes

class Calculadora:
    def __init__(self):
        self.janela = ttkthemes.ThemedTk()
        self.janela.set_theme("equilux")  # Tema escuro
        self.janela.title("Calculadora")
        self.janela.configure(bg='#2e2e2e')
        
        # Variável para armazenar a expressão
        self.expressao = ""
        
        # Campo de entrada
        self.entrada = ttk.Entry(self.janela, justify="right", font=("Arial", 20))
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Botões
        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        
        for botao in botoes:
            cmd = lambda x=botao: self.click(x)
            ttk.Button(self.janela, text=botao, command=cmd).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
                
        # Botão Clear
        ttk.Button(self.janela, text="C", command=self.clear).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
        # Configurar o redimensionamento
        for i in range(4):
            self.janela.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.janela.grid_rowconfigure(i, weight=1)
            
    def click(self, valor):
        if valor == '=':
            try:
                resultado = eval(self.expressao)
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, resultado)
                self.expressao = str(resultado)
            except:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, "Erro")
                self.expressao = ""
        else:
            self.expressao += valor
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, self.expressao)
            
    def clear(self):
        self.expressao = ""
        self.entrada.delete(0, tk.END)
        
    def iniciar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    calc = Calculadora()
    calc.iniciar()