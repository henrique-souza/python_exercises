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

print(colors)
#print(type(colors))
print('\n')

print('Programa 02')
# pode-se adicionar valores de qualquer tipo
# não é preferível, nem prático
print('Imprimindo a lista "sundry"')
sundry = ['Henrique', 3.14, 7, False]

print(sundry)
#print(type(sundry))
print('\n')

print('Programa 03')

print(f'Toda lista começa com 0. Portanto o segundo item de "colors", que seria o numero 1, é: {colors[1]}')
print(f'\nSendo assim, para buscar meu nome, utilizarei o local 0 na lista: {sundry[0]}')
print(f'\nUltimo item da lista "colors": {colors[-1]}')
print(f'Ultimo item da lista "sundry": {sundry[-1]}')
print(f'\nPenultimo item da lista "colors" {colors[-2]}')
print(f'Penultimo item da lista "sundry" {sundry[-2]}')
print('\n')
# parei na Etapa 3, unidade 2