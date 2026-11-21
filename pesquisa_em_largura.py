from collections import deque

fila_de_pesquisa = deque()
fila_de_pesquisa += grafo["voce"]

while fila_de_pesquisa:
    pessoa = fila_de_pesquisa.popleft()
    if pessoa_e_vendedor(pessoa):
        print(pessoa + " é um vendedor de manga!")
        return True
    else:
        fila_de_pesquisa += grafo[pessoa]
return False

def pessoa_e_vendedor(nome):
    return nome[-1] == "m"
