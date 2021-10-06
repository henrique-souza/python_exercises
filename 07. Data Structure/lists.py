# caso queira testar os programas separadamente, adicione
# comentários de apóstofos simples ''' e ''' ENTRE um programa e outro.
# Exemplo abaixo:

'''
print('Programa X')
código

'''

print('Programa 01')
# uma lista
print('Imprimindo a lista "colors"')
colors = ['vermelho', 'verde', 'azul', 'amarelo', 'laranja', 'roxo', 'marrom']
colors2 = ['vermelho', 'verde', 'azul']

print(colors)
# print(type(colors))
print('\n')

print('Programa 02')
# pode-se adicionar valores de qualquer tipo
# não é preferível, nem prático
print('Imprimindo a lista "sundry"')
sundry = ['Henrique', 3.14, 7, False]

print(sundry)
# print(type(sundry))
print('\n')
'''
print('Programa 03')

print(
    f'Toda lista começa com 0. Portanto o segundo item de "colors", que seria o numero 1, é: {colors[1]}')
print(
    f'\nSendo assim, para buscar meu nome, utilizarei o local 0 na lista: {sundry[0]}')
print(f'\nUltimo item da lista "colors": {colors[-1]}')
print(f'Ultimo item da lista "sundry": {sundry[-1]}')
print(f'\nPenultimo item da lista "colors" {colors[-2]}')
print(f'Penultimo item da lista "sundry" {sundry[-2]}')
print('\n')

print('Programa 04')
# imprimindo um índice inexistente na lista de dados
print('\nPara rodar o 04, remova o comentário da linha 46.')
# Irá imprimir o erro 'IndexError: list index out of range', pois "colors2" vai de 0 a 2
# na numeração de seus índices.
# print(colors2[3])
print('\n')
'''

print('Programa 05')

print('\nImprime uma fatia, começando no índice 2 e excluindo o índice 5: ')
print(colors[2:5])
print(type(colors[2:5]))

print('\nImprime uma fatia, começando no índice 0 até o índice 3:')
print(colors[:3])

print('\nImprime uma fatia, começando pelo índice 4 e indo até o fim da lista:')
print(colors[4:])

print('\nImprime uma fatia, da 4th até o final da lista (mas não o último item):')
print(colors[-4:-1])
print('\n')
#parei na Etapa 4
