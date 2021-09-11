# Remova estes primeiros apóstofos e coloque-os ANTES/ACIMA dos
# comentários "# programa X" e execute as linhas que deseja testar

''' 
#programa 01

#testando a função type(), que expressa que tipo de dados estou trabalhando

print(type('Olá mundo!')) #imprime str
print(type(7)) #imprime int

print(type(True)) #imprime bool
print(type(False)) #imprime bool

print(type('True')) #imprime str
print(type('False')) #imprime str

#programa 02

#agora irei testar a função bool(), irá imprimir se os valores setados são True ou False

print(bool('True'))
print(bool('False'))
print(bool('')) #cadeia de carcteres vazia, logo, False
print(bool(' '))
print(bool('Olá mundo!'))

#programa 03

print(bool(7))
print(bool(1))
print(bool(0)) #este valor não sendo diferente de 0, imprimirá False
print(bool(-1))

#programa 04

print(1 + 1 == 3) #vai imprimir um False    
print(1 + 1 == 2) #vai imprimir um True 

#programa 05

#vai imprimir quais operações são False ou True
print(3 == 4)
print(3 != 4)
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
'''
#programa 06

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
