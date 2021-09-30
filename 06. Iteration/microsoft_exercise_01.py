import random

roll = 0
count = 0

# iniciando o laço 'roll' enquanto os dados forem diferentes de 5
while roll != 5:
    # joga na tela os números de 1 a 5, até que apareça 5
    print(f'\nSorteio {count + 1}')
    # 'count' conta quantas vezes os números foram sortidos
    count = count + 1
    # sorteia os números de 1 a 5
    roll = random.randint(1, 5)
    # printa o resultado randomico de 'roll'
    print(f'Resultado: {roll}')
print(f'\nDepois de {count} jogadas, conseguimos obter um 5!')
print('\n')
