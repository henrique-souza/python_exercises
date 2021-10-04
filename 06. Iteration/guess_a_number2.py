# Solução - Henrique Souza
# objetivo: fazer um jogo de adivinhação, mas desta vez:
# 1. Exiba o número da tentativa atual.
# 2. Se o número fornecido for muito baixo, informe ao usuário "Este número é muito baixo, tente novamente!"
# 3. Se o número fornecido for muito alto, informe ao usuário "Este número é muito alto, tente novamente!"
# 4. Se o usuário inserir um valor não numérico, informe "Somente números."

import random

numbers = random.randint(1, 5)
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
    print(f'\nVocê adivinhou o número em {count} tentativas.')
