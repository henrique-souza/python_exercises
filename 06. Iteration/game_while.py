import random

# este programa é como um jogo que sorteia de números de 1 a 5
# até que se obtenha um 5. Ganha quem sortear o número 5 primeiro.
# podem ser mais de um jogador, desde que respeite-se a ordem.
roll = 0
count = 0

print('O primeiro que sortear um 5 vence!!')
# iniciando o laço enquanto o valor da variável 'roll' for diferente de 5
while roll != 5:
    print('\n')
    name = input('Digite seu nome ou \'q\' para sair do jogo:  ')
    
    #se a entrada do usuario pra 'name' for um Enter ou espaço em branco
    if name.strip() == '':
        # o programa continuará solicitando entrada de um nome
        continue
    
    if name.strip() == 'q':
        break
    
    # se a variavel 'count' começa com 0, a partir deste print começara com 1
    # contando assim a quantidade de sorteios corretamente
    print(f'Sorteio {count + 1} - {name}')
    # 'count' conta quantas vezes os números foram sortidos
    count = count + 1
    # sorteia os números de 1 a 5
    roll = random.randint(1, 5)
    # printa o resultado randomico de 'roll' até que apareça 5
    print(f'{name} sorteou: {roll}')
else:
    print('\n')
    print(f'{name} Ganhou!!!')
print(f'\nO jogo sorteou {count} números!')
