# Solução - Henrique Souza
# objetivo: fazer um jogo de adivinhação, mas desta vez:
# 1. Exiba o número da tentativa atual.
# 2. Se o número fornecido for muito baixo, informe ao usuário "Este número é muito baixo, tente novamente!"
# 3. Se o número fornecido for muito alto, informe ao usuário "Este número é muito alto, tente novamente!"
# 4. Se o usuário inserir um valor não numérico, informe "Somente números."

import random

numbers = random.randint(1, 10)
choice = 0
count = 0

print('Jogo de adivinhação!\n\nAdivinhe um número entre 1 e 10')

while choice != numbers:
    print('\n')

    count += 1

    choice = input(f'Tentativa #{count}: ')

    # este laço faz com que, mesmo que o usuário digite Enter, nomes ou símbolos
    # o jogo continua sendo executado, sem problemas.
    if choice.isnumeric():

        choice = int(choice)
    else:
        print('\nATENÇÃO: Digite apenas números de 1 a 10.')
        continue

    if choice > numbers:
        print('Sua adivinhação é muito alta, tente novamente.')
    
    if choice < numbers:
        print('Sua adivinhação é muito baixa, tente novamente!')

else: 
    print(f'\nVocê adivinhou o número em {count} tentativas.')
# Jogo da adivinhação fazendo o que se pede, veremos abaixo o que a Microsoft
# sugere como solução para os objetivos propostos.

'''
Solução - Microsoft

import random

value = random.randint(1, 10)
count = 0
guess = 0
print('Guess a number between 1 and 10')

while guess != value:
    count += 1
    guess = input(f'Enter guess #{count}: ')

    if guess.isnumeric():
        guess = int(guess)
    else:
        print('Numbers only, please!')
        continue

    if guess > value:
        print('Your guess is too high, try again!')
    elif guess < value:
        print('Your guess is too low, try again!')

else:
    print(f'You guessed it in {count} tries!')

'''
