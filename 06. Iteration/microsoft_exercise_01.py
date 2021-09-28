import random

roll = 0
count = 0

while roll != 5: # enquanto roll for diferente de 5
    print(f'Sorteio {count + 1}')  # joga na tela os números de 1 a 5, até que apareça 5.
    count = count + 1  
    ''' a variável count faz a conta de quantas vezes
    os números foram sortidos até chegar o número 5
    e depois exibe o total na linha 12 '''
    roll = random.randint(1, 5)  # sorteia os números de 1 a 5
    print(f'Resultado: {roll}')  # joga na tela os números de 1 a 5, até que apareça 5.
    print('\n')
print(f'\nDepois de {count} jogadas, conseguimos obter um 5!')
