from random import randint
from time import sleep

# Lista temporária para armazenar números sorteados.
lista = list()

# Lista para armazenar os jogos gerados.
jogos = list()

# Mensagem visual.
print('-' * 30)
print('         JOGA NA LOTO FÁCIL         ')
print('-' * 30)

# Solicita ao usuário a quantidade de jogos desejada.
quantidade = int(input('Quantos jogos quer sortear? '))

# Variável para contar o total de jogos gerados.
total = 1

# Loop principal para gerar os jogos.
while total <= quantidade:
    # Inicializa a contagem de números únicos para cada jogo.
    contagem = 0
    
    # Loop interno para gerar 15 números únicos para cada jogo.
    while True:
        # Gera um número aleatório entre 1 e 25.
        numero = randint(1, 25)
        
        # Verifica se o número já foi sorteado.
        if numero not in lista:
            # Adiciona o número à lista temporária.
            lista.append(numero)
            
            # Incrementa a contagem de números únicos.
            contagem += 1
        
        # Se atingiu 15 números únicos, sai do loop interno.
        if contagem >= 15:
            break
    
    # Ordena a lista temporária em ordem crescente.
    lista.sort()
    
    # Adiciona uma cópia da lista temporária à lista de jogos.
    jogos.append(lista[:])
    
    # Limpa a lista temporária para o próximo jogo.
    lista.clear()
    
    # Incrementa o total de jogos gerados.
    total += 1

# Mensagem indicando que os jogos estão sendo sorteados.
print('-=' * 6, f'SORTEANDO {quantidade} JOGOS', '-=' * 6)

# Imprime cada jogo numerado com pausa de 1 segundo entre cada impressão.
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)

# Mensagem desejando boa sorte.
print('-=' * 9, '< BOA SORTE!!! >', '-=' * 9)
