# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Informações: 
# - Uma calculadora simples com as operações: soma, divisão, subtração, multiplicação, porcentagem.
# - Opções extra: apagar, deletar, finalizar operação, adicionar ponto

# Fluxo: 
# O usuário deve ser capaz tanto de digitar quanto de selecionar os componentes para sua fórmula.

# Medidas:
# - Tamanho da janela: 300x400
# - Grid da calculadora: 5x4

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



import tkinter as tk


# Janela principal
janela = tk.Tk()
janela.title(" - Calculadora - ")

# Tamanho da janela
janela.geometry("300x400")


# Visor 
visor = tk.Entry(janela, font = ('Arial', 20), justify = 'right')
visor.grid(row = 0, columnspan = 4, sticky = 'nsew')


# Configuração do grid das colunas ( 4 colunas )
janela.grid_columnconfigure(0, weight = 1)
janela.grid_columnconfigure(1, weight = 1)
janela.grid_columnconfigure(2, weight = 1)
janela.grid_columnconfigure(3, weight = 1)


# Botões => texto
botoes = [
    'C', '<', '%', '/',
    '7', '8', '9', 'x',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
       '0'  , '.', '=',
]





# Função de clique = quando clicado um dos botões insira o texto dele
def clicou(t):

    if t == '=':
        print('Calculando ... ')
        pass
    elif t == 'C':
        print('Deletando ... ')

        visor.delete(0, tk.END)
        pass
    elif t == '<':
        print('Apagando último item ... ')

        # Pegando último indice (0,1,2,3,4 = [5])
        ultimo = len(visor.get()) - 1
        visor.delete(ultimo, tk.END)
        pass

    else: visor.insert(tk.END, t)


# expressao = visao.get()
# resultado = eval(expressao)



# Medidas iniciais
linha  = 1
coluna = 0

# Loop de contrução
for texto in botoes:

    botao = tk.Button(janela, text=texto, command=lambda t=texto: clicou(t))

    if texto == '0':
        coluna += 2
        botao.grid(row=linha, columnspan=coluna, sticky='nsew')

    else: 
        botao.grid(row=linha, column=coluna, sticky='nsew')
        coluna += 1

    # => Quebra de linha
    if coluna > 3 : 
        coluna = 0
        linha += 1

    if linha > 5 : break







# Manter a janela aberta (mainloop)
janela.mainloop()