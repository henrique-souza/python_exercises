import random

roll = 0
count = 0

# iniciando o laço enquanto o valor da variável 'roll' forem diferentes de 5
while roll != 5:
    # se a variavel 'count' começa com 0, a partir deste print começara com 1
    # contando assim a quantidade de sorteios corretamente
    print(f'Sorteio {count + 1}')
    # 'count' conta quantas vezes os números foram sortidos
    count = count + 1
    # sorteia os números de 1 a 5
    roll = random.randint(1, 5)
    # printa o resultado randomico de 'roll' até que apareça 5
    print(f'Resultado: {roll}')
    print('\n')
print(f'\nDepois de {count} jogadas, conseguimos obter um 5!')
print('\n')
