# caso queira testar os programas separadamente, adicione
# comentários de apóstofos simples ''' e ''' ENTRE um programa e outro.
# Exemplo abaixo:
'''

print('Programa X')
código

'''

print('Programa 01\n')

remedio = 'Dorflex'
dosagem = 5
duracao = 4.5

instrucoes = '{} - Tome {} ML pela boca a cada {} horas'.format(
    remedio, dosagem, duracao)
print(instrucoes)

instrucoes = '{2} - Tome {1} ML pela boca a cada {0} horas'.format(
    remedio, dosagem, duracao)
print(instrucoes)

instrucoes = '{remedio} - Tome {dosagem} ML pela boca a cada {duracao} horas'.format(
    remedio='Dipirona', dosagem=10, duracao=6)
print(instrucoes)
print('\n')

print('Programa 02\n')

nome = 'mundo'
mensagem = f'Olá, {nome}.'
print(mensagem)

contagem = 10
valor = 3.14
mensagem = f'Contagem até {contagem}. Multiplique por {valor}.'
print(mensagem)
print('\n')

print('Programa 03\n')

width = 5
height = 10
print(
    f'O perímetro é {(2 * width) + (2 * height)} e a área é {width * height}.')
print('\n')


print('Programa 04\n')

valor = 'Olá'

print(f'.{valor:<50}.')
print(f'.{valor:>50}.')
print(f'.{valor:^50}.')
print(f'.{valor:_^50}.')
print('\n')
