# caso queira testar os programas separadamente, adicione
# comentários de apóstofos simples ''' e ''' ENTRE um programa e outro.
# Exemplo abaixo:

'''
print('Programa X\n')
código
print('\n')

'''

print('Programa 01\n')

first_value = 5
second_value = 4

sum = first_value + second_value
difference = first_value - second_value
product = first_value * second_value
quotient = first_value / second_value
modulus = first_value % second_value
exponent = first_value ** second_value

print('Sum: ' + str(sum))
print('Difference: ' + str(difference))
print('Product: ' + str(product))
print('Quotient: ' + str(quotient))
print('Modulus: ' + str(modulus))
print('Exponent: ' + str(exponent))
print('\n')

print('Programa 02\n')
# testando acrônimo PEMDAS (Parenteses, Expoentes, Multiplicação
# Divisão, Adição, Subtração), que indica a ordem que
# as operações em Python são realizadas

print(3 + 4 * 5)
print((3 + 4) * 5)
print('\n')

print('Programa 03\n')

first_value = 5
second_value = 4

quotient = first_value / second_value

print(type(quotient))
print(quotient)
print('\n')

print('Programa 04\n')

pi = 3.14
print(type(pi))
print(int(pi))
print(round(pi))

uptime = 99.99
print(type(uptime))
print(int(uptime)) # irá sair um numero 99
print(round(uptime)) # irá arredondar o float para um
print('\n')

print('Programa 05\n')

first_value = round(7.654321, 2) # fazendo arredondamento sair com 2 casas decimais
print(first_value)

second_value = round(9.87654, 3) # fazendo sair com 3 casas decimais
print(second_value)
print('\n')

