# Módulos
from random import randint
from time import sleep

# Lista
lista = list()

# Jogos
jogos = list()

# Titulo
print('-' * 30)
print('         JOGA NA LOTO FÁCIL         ')
print('-' * 30)

# Pergunta
quantidade = int(input('Quantos jogos quer sortear? '))
""" Quantidade de jogos. """
total = 1

# Sorteio
while total <= quantidade:
    contagem = 0
    """ Contagem de jogos. """
    while True:
        """ Sorteio de números. """
        numero = randint(1, 25)
        if numero not in lista:
            """ Verifica se o número já existe. """
            lista.append(numero)
            """ Adiciona o número na lista. """
            contagem += 1
        if contagem >= 15:
            """ Verifica se o número de números sorteados é igual a 15. """
            break
            """ Sai do loop. """
    lista.sort()
    """ Ordena a lista. """
    jogos.append(lista[:])
    """ Adiciona a lista na lista de jogos. """
    lista.clear()
    """ Limpa a lista. """
    total += 1
    """ Contagem de jogos. """
print('-=' * 6, f'SORTEANDO {quantidade} JOGOS', '-=' * 6)
for i, l in enumerate(jogos):
    """ Imprime os jogos. """
    print(f'Jogo {i + l}: {l}')
    sleep(1)
