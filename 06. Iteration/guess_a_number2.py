# Solução - Henrique Souza
# objetivo: fazer um jogo de adivinhação, mas desta vez:
# 1. Exiba o número da tentativa atual.
# 2. Se o número fornecido for muito baixo, informe ao usuário "Este número é muito baixo, tente novamente!"
# 3. Se o número fornecido for muito alto, informe ao usuário "Este número é muito alto, tente novamente!"
# 4. Se o usuário inserir um valor não numérico, informe "Somente números."

import random

randomic_value = random.randint(1, 10)
user_choice = 0
tentative_count = 0

print('Jogo de adivinhação!\n\nAdivinhe um número entre 1 e 10')

# enquanto a escolha do usuário (user_choice) for diferente do número sorteado (randomic_value)
# o laço while: será chamado
while user_choice != randomic_value:

    print('\n')
    # o comando faz a contagem de tentativas do usuário
    tentative_count += 1

    # entrada dos dados pelo usuário
    user_choice = input(f'Tentativa #{tentative_count}: ')

    if user_choice.isnumeric():

        # este comando faz com que as entradas do usuário sejam
        # convertidas em int()
        user_choice = int(user_choice)

    # este laço faz com que, mesmo que o usuário digite Enter, nomes ou símbolos
    # o jogo continua sendo executado, sem mensagens de erro.
    else:
        print('\nATENÇÃO: Digite apenas números de 1 a 10.')
        continue

    # se a escolha do usuário for maior que o número sorteado
    if user_choice > randomic_value:

        # irá impimir esta mensagem na tela.
        print('Sua adivinhação é muito alta, tente novamente.')

    # se a escolha do usuário for menor que o número sorteado
    if user_choice < randomic_value:

        # irá imprimir esta mensagem na tela.
        print('Sua adivinhação é muito baixa, tente novamente!')

# se o usuário adivinhar o número que foi armazenado em (randomic_value) na jogatina
else:

    # a mensagem abaixo será posta na tela.
    print(f'\nVocê adivinhou o número em {tentative_count} tentativas.')

    
# Jogo da adivinhação fazendo o que se pede, veremos abaixo o que a Microsoft
# sugere como solução para os objetivos propostos.

'''
Solução - Microsoft

import random

value = random.randint(1, 10)
tentative_count = 0
guess = 0
print('Guess a number between 1 and 10')

while guess != value:
    tentative_count += 1
    guess = input(f'Enter guess #{tentative_count}: ')

    if guess.isnumeric():
        guess = int(guess)
    else:
        print('randomic_value only, please!')
        continue

    if guess > value:
        print('Your guess is too high, try again!')
    elif guess < value:
        print('Your guess is too low, try again!')

else:
    print(f'You guessed it in {tentative_count} tries!')

'''
