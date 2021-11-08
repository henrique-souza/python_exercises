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
print('\nPara rodar o 04, remova o comentário da linha 46 e comente esta linha.')
# Irá imprimir o erro 'IndexError: list index out of range', pois "colors2" vai de 0 a 2
# na numeração de seus índices.
# print(colors2[3])
print('\n')


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

print('Programa 06')

# esta função reverte a ordem da lista
colors.reverse()
print('Invertendo a ordem da lista: \n', colors, '\n')

# esta função classifica a lista em ordem alfabética
colors.sort()
print('Classificando a lista em ordem alfabética: \n', colors)
print('\n')

print('Programa 07')

# iremos tratar a lista como uma fila neste momento, pois a função 'pop()' 
# faz com que seja recolhido um dado naquela determinada coordenada

# a função pop(0) recolhe a cor cadastrada no inicio da lista de cores
color = colors.pop(0)
print('Recolhendo uma cor do início da lista: ', color, '\n')
print('Lista atual, sem a cor recolhida no começo: ')
print(colors)

# a função pop(-1) recolhe a cor cadastrada no fim da lista (fila) de cores
color = colors.pop(-1)
print('Recolhendo uma cor do fim da fila: ', color, '\n')
print('Fila atual, sem a cor recolhida no fim: ')
print(colors)

# nesta linha iremos imprimir a lista (fila) de cores armazenadas após a função 'pop()'
print('Fila atual, sem as cores recolhidas no começo e fim: ')
print(colors)
print('\n')
