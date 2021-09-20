# caso queira testar os programas separadamente, adicione
# comentários de apóstofos simples ''' e ''' ENTRE um programa e outro.
# Exemplo abaixo:

'''
print('Programa X')
código

'''

print('Programa 01')

print(type('7'))
print(type(7))
print(type(7.1))
print('\n')

print('Programa 02')

print(isinstance('7', str))
print(isinstance(7, int))
print(isinstance(7.1, float))

print(isinstance(7, str))
print(isinstance('7', int))
print(isinstance('7.1', float))
print('\n')

print('Programa 03')

print(type('7') == str)
print(type(7) == int)
print(type(7.1) == float)

print(type(7) == str)
print(type('7') == int)
print(type('7.1') == float)
# não é tão recomendado usar a função type(), principalmente quando começar a
# ver POO com Python
print('\n')


print('Programa 04')

x = 'uma string'
print(type(x))
x = 7
print(type(x))
x = False
print(type(x))
print('\n')
