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
colors2 = ['lilás', 'cinza', 'rosa']

print(colors)
print(type(colors))
print('\n')

print('Programa 02')
# pode-se adicionar valores de qualquer tipo
# não é preferível, nem prático
print('Imprimindo a lista "sundry"')
sundry = ['Henrique', 3.14, 7, False]

print(sundry)
print(type(sundry))
print('\n')

print('Programa 03')

print(
    f'Toda lista começa com 0. Portanto o segundo item de "colors", que seria o numero 1, é: {colors[1]}')
print(
    f'\nSendo assim, para buscar meu nome em "sundry", utilizarei o local 0 na lista: {sundry[0]}')
print(f'\nUltimo item da lista "colors": {colors[-1]}')
print(f'Ultimo item da lista "sundry": {sundry[-1]}')
print(f'\nPenultimo item da lista "colors" {colors[-2]}')
print(f'Penultimo item da lista "sundry" {sundry[-2]}')
print('\n')

print('Programa 04')
# imprimindo um índice inexistente na lista de dados
print('\nPara rodar o 04, remova o comentário da linha 48 e comente esta linha.')
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

""" print('Programa 07')

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
print('\n') """

print('Programa 08')

# neste programa, iremos adicionar ou remover dados da lista
# como nós queremos nossa lista de cores de volta, devemos comentar o programa 07 acima
# caso queira o programa sem a classificação em ordem alfabética, comente o programa 06

print(colors)
print('\nCaso você queira ver, do Programa 08 em diante, funcionando, comente todo o programa 07 acima.\n')
# adicionando preto e branco
colors.append('preto')  # adicionado ao fim da lista
colors.append('branco')  # adicionado ao fim da lista

# removendo amarelo e laranja
colors.remove('amarelo')
colors.remove('laranja')

print(colors)
# simbora gerar um erro? Caso queira ver
# remova o comentario da linha 121

# irá imprimir um 'ValueError'
# colors.remove('qualquer coisa')
print('\n')

print('Programa 09')
# neste programa iremos unir as listas armazenadas até aqui
# gostaria mundo de unir a lista 'sundry', mas como ela usa
# de más práticas, não iremos puxa-la.

#vamos imprimir colors atual, pra fins de comparação
print(colors)

# nova lista 'colors3'
colors3 = ['limão', 'beje']
# unindo 'colors' com 'colors2'
colors.extend(colors2)
# unindo 'colors' e 'colors2' com 'colors3'
colors.extend(colors3)

# eu tive vontade de classificar em ordem alfabética a partir daqui, foi mal. Pra ficar bonito.
colors.sort()
print(colors)

print('\n')
#parei na etapa 9
