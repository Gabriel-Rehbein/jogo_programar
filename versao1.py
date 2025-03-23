import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Treinamento em Programação")
        self.root.geometry("800x600")

        # Estilo
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=5)
        style.configure("TLabel", font=("Arial", 14))
        style.configure("Menu.TFrame", background="#f5f5f5")
        style.configure("Main.TFrame", background="#ffffff")

        # Menu lateral
        self.menu_frame = ttk.Frame(self.root, width=200, style="Menu.TFrame")
        self.menu_frame.pack(side='left', fill='y')

        self.btn_desafios = ttk.Button(self.menu_frame, text="Desafios", command=self.mostrar_desafios)
        self.btn_desafios.pack(fill='x', pady=10)

        self.btn_quizzes = ttk.Button(self.menu_frame, text="Quizzes", command=self.mostrar_quizzes)
        self.btn_quizzes.pack(fill='x', pady=10)

        self.btn_comunidade = ttk.Button(self.menu_frame, text="Comunidade", command=self.mostrar_comunidade)
        self.btn_comunidade.pack(fill='x', pady=10)

        # Área principal
        self.main_frame = ttk.Frame(self.root, style="Main.TFrame")
        self.main_frame.pack(side='right', fill='both', expand=True)

        self.inicializar_pagina_inicial()

    def inicializar_pagina_inicial(self):
        """Exibe uma tela inicial ao abrir o software."""
        self.limpar_main_frame()
        ttk.Label(self.main_frame, text="Bem-vindo ao Treinamento em Programação!", font=('Arial', 20), anchor="center").pack(pady=20)
        ttk.Label(self.main_frame, text="Escolha uma opção no menu ao lado para começar.", font=('Arial', 14), anchor="center").pack(pady=10)

    def mostrar_desafios(self):
        """Exibe a seção de desafios."""
        self.limpar_main_frame()
        ttk.Label(self.main_frame, text="Desafios de Programação", font=('Arial', 20)).pack(pady=20)

        desafios = [
            "1. Crie uma função que retorne o reverso de uma string.",
            "2. Desenvolva um algoritmo para calcular a soma de números de 1 a N.",
            "3. Escreva um programa que encontre números primos em um intervalo.",
            "4. Construa uma função que classifique uma lista de números.",
            "5. Faça um programa que converta temperaturas de Celsius para Fahrenheit."
        ]

        for desafio in desafios:
            ttk.Label(self.main_frame, text=desafio, font=('Arial', 12)).pack(anchor='w', pady=5)

    def mostrar_quizzes(self):
        """Exibe a seção de quizzes."""
        self.limpar_main_frame()
        ttk.Label(self.main_frame, text="Quizzes Interativos", font=('Arial', 20)).pack(pady=20)

        quizzes = [
            "1. Qual é a saída de print(2**3)? \n a) 6 \n b) 8 \n c) 9",
            "2. Qual é o tipo de dado do resultado de 5/2 em Python? \n a) int \n b) float \n c) str",
            "3. Qual a função usada para obter a entrada do usuário em Python? \n a) input() \n b) print() \n c) scanf()",
            "4. Como você comenta uma linha em Python? \n a) # comentário \n b) // comentário \n c) /* comentário */",
            "5. Qual operador verifica se dois valores são iguais? \n a) == \n b) != \n c) ="
        ]

        for quiz in quizzes:
            ttk.Label(self.main_frame, text=quiz, font=('Arial', 12)).pack(anchor='w', pady=5)

    def mostrar_comunidade(self):
        """Exibe a seção de comunidade."""
        self.limpar_main_frame()
        ttk.Label(self.main_frame, text="Comunidade Offline", font=('Arial', 20)).pack(pady=20)
        ttk.Label(self.main_frame, text="Aqui será possível ver e compartilhar soluções.", font=('Arial', 14)).pack(pady=10)

    def limpar_main_frame(self):
        """Remove todos os widgets da área principal."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
