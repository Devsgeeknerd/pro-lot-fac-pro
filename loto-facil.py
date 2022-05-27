# Módulos
from random import randint
from time import sleep

# Lista
lista = list()

# Jogos
jogos = list()

# Titulo
print('-' * 60)
print('        JOGA NA LOTO FÁCIL        ')
print('-' * 60)

# Pergunta
quantidade = int(input('Quantos jogos você quer gerar? '))
total = 1

# Sorteando os números
while total <= quantidade:
    contagem = 0
    while True:
        numero = randint(1, 25)
        if numero not in lista:
            lista.append(numero)
            contagem += 1
        if contagem >= 15:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-' * 6, f' SORTEANDO {quantidade} JOGOS ', '-' * 6)
