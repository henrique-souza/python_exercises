# Solução - Henrique Souza
# objetivo: fazer um jogo de adivinhação
# o programa estará sorteando números de 1 a 5
# o usuario irá digitar um numero de 1 a 5 e tentar adivinhar
import random

numbers = random.randint(1, 5)
choice = 0
count = 0

print('Jogo de adivinhação!')
# programa corrigido depois de ver o exemplo da Microsoft.
# Consulte os commits para ver as versões anteriores a resposta
while choice != numbers:
    print('\n')

    count += 1

    print(f'Jogada número: {count}')

    choice = input(
        'Digite um numero entre 1 a 5 ou \'sair\' para sair do jogo: ')

    # este laço faz com que, mesmo que o usuário digite Enter, nomes ou símbolos
    # o jogo continua sendo executado, sem problemas.
    if choice.isnumeric():

        choice = int(choice)
else:
    print(f'\nVocê adivinhou em o número {count} tentativas.')

'''
# Solução - Microsoft abaixo:

# Irei corrigir o programa acima

import random

value = random.randint(1, 5)
count = 0
guess = 0

while guess != value:

    count += 1
    guess = input('Guess a number between 1 and 5: ')

    if guess.isnumeric():
        guess = int(guess)
else:
    print(f'You guessed it in {count} tries!')
'''
