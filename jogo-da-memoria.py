import tkinter as tk
from tkinter import messagebox
import random

# Configurações do jogo
NUM_LINHAS = 4
NUM_COLUNAS = 4
WIDTH = 10
HEIGHT = 10
CORES = ['#FF0000', '#0000FF', '#00FF00', '#FFFF00',
         '#800080', '#FFA500', '#00FFFF', '#FF00FF']

COR_BACKGROUND = "#343a40"
COR_LETRA = '#ffffff'
FONTE_STYLE = ('Arial', 12, 'bold')
MAX_TENTATIVAS = 25

cartoes = []
cartao_revelado = []
cartao_correspondes = []
numeros_tentativas = 0


def Application():

    # Função para criar a grade de cores aleatórias
    def create_card_grid():
        cores = CORES * 2
        random.shuffle(cores)
        return [cores[i:i+NUM_COLUNAS] for i in range(0, len(cores), NUM_COLUNAS)]

    # Função para tratar o clique em um cartão
    def card_clicked(linha, coluna):
        cartao = cartoes[linha][coluna]
        cor = cartao['bg']
        if cor == 'black':
            cartao['bg'] = grid[linha][coluna]
            cartao_revelado.append(cartao)
            if len(cartao_revelado) == 2:
                check_match()

    # Função para verificar se dois cartões combinam
    def check_match():
        primeiro_cartao, segundo_cartao = cartao_revelado
        if primeiro_cartao['bg'] == segundo_cartao['bg']:
            for cartao in [primeiro_cartao, segundo_cartao]:
                cartao.after(1000, cartao.destroy)
                cartao_correspondes.append(cartao)
            check_win()
        else:
            for cartao in [primeiro_cartao, segundo_cartao]:
                cartao.after(1000, lambda c=cartao: c.config(bg='black'))
        cartao_revelado.clear()
        update_score()

    # Função para verificar se o jogador venceu
    def check_win():
        if len(cartao_correspondes) == NUM_LINHAS * NUM_COLUNAS:
            messagebox.showinfo('Parabéns!', 'Você ganhou o jogo!')
            janela.quit()

    # Função para atualizar a contagem de tentativas
    def update_score():
        global numeros_tentativas
        numeros_tentativas = numeros_tentativas + 1
        label_tentativas.config(
            text=f'Tentativas: {numeros_tentativas}/{MAX_TENTATIVAS}')
        if numeros_tentativas >= MAX_TENTATIVAS:
            messagebox.showinfo('Fim de jogo', 'Você perdeu o jogo!')

    # Interface Principal
    janela = tk.Tk()
    janela.title('Jogo da Memória')
    janela.configure(bg=COR_BACKGROUND)

    grid = create_card_grid()

    for linha in range(NUM_LINHAS):
        linha_cartoes = []
        for col in range(NUM_COLUNAS):
            cartao = tk.Button(janela, width=WIDTH, height=HEIGHT, bg='black',
                               relief=tk.RAISED, bd=3, command=lambda r=linha, c=col: card_clicked(r, c))
            cartao.grid(row=linha, column=col, padx=5, pady=5)
            linha_cartoes.append(cartao)
        cartoes.append(linha_cartoes)

    # Personalização dos botões
    button_style = {'activebackground': '#f8f9fa',
                    'font': FONTE_STYLE, 'fg': COR_LETRA}
    janela.option_add('*Button', button_style)

    # Label para a contagem de tentativas
    label_tentativas = tk.Label(
        janela, text=f'Tentativas: {numeros_tentativas}/{MAX_TENTATIVAS}', fg='white', bg=COR_BACKGROUND, font=FONTE_STYLE)
    label_tentativas.grid(
        row=NUM_LINHAS, columnspan=NUM_COLUNAS, padx=10, pady=10)

    janela.mainloop()


if __name__ == '__main__':
    Application()
