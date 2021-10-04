import random

numbers = 0

print('Jogo de adivinhação!')

while numbers != 5:
    print('\n')
    choice = input('Digite um numero de 1 a 5: ')

    if choice.strip() == '':
        continue
