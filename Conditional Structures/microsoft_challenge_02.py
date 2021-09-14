# caso queira testar os programas separadamente, adicione
# comentários de apóstofos simples ''' e ''' ENTRE um programa e outro.
#Exemplo abaixo:
'''

print('Programa X')
código

'''

print('Programa 01\n')

#testando a função type(), que expressa que tipo de dados estou trabalhando

print(type('Olá mundo!')) #imprime str
print(type(7)) #imprime int
print(type(True)) #imprime bool
print(type(False)) #imprime bool
print(type('True')) #imprime str
print(type('False')) #imprime str
print('\n')

print('Programa 02\n')

#agora irei testar a função bool(), irá imprimir se os valores setados são True ou False
print(bool('True'))
print(bool('False'))
print(bool('')) #cadeia de carcteres vazia, logo, False
print(bool(' '))
print(bool('Olá mundo!'))
print('\n')

print('Programa 03\n')

print(bool(7))
print(bool(1))
print(bool(0)) #este valor não sendo diferente de 0, imprimirá False
print(bool(-1))
print('\n')

print('Programa 04\n')

print(1 + 1 == 3) #vai imprimir um False    
print(1 + 1 == 2) #vai imprimir um True 
print('\n')

print('Programa 05\n')

#vai imprimir quais operações são False ou True
print(3 == 4)
print(3 != 4)
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print('\n')

print('Programa 06\n')

primeiro_numero = 5
segundo_numero = 0
valor_true = True
valor_false = False

if primeiro_numero > 1 and primeiro_numero < 10:
    print('O valor está entre 1 e 10.')

if primeiro_numero > 1 or segundo_numero > 1:
    print('Pelo menos um dos valores digitados é maior que 1')

print(not valor_true)
print(not valor_false)

if not primeiro_numero > 1 and segundo_numero < 10:
    print('Ambos valores passaram no teste.')
else:
    print('Ambos valores NÃO passaram no teste.')
