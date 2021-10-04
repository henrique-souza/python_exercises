# objetivo: fazer um jogo de adivinhação
# o programa estará sorteando números de 1 a 5
# o usuario irá digitar um numero de 1 a 5 e tentar adivinhar 
import random

numbers = 0
count = 0

print('Jogo de adivinhação!')

while numbers != 5:
    print('\n')

    count += 1

    print(f'Jogada número: {count}')

    choice = input('Digite um numero entre 1 a 5 ou \'sair\' para sair do jogo: ')

    # este laço faz com que, mesmo que o usuário digite Enter, nomes ou símbolos
    # o jogo continue rodando, sem problemas.
    if choice.strip() == '':
        continue
    # dando opções para fechar o jogo ao usuário, em 2 línguas.
    if choice.strip() == 'exit' or choice.strip() == 'sair':
        break

    # existe algum bug com a função random()
    # está randomizando além de 1 a 5
    numbers = random.randint(1, 5)

print(f'\nVocê adivinhou em o número {count} tentativas.')