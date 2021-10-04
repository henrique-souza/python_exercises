# caso queira testar os programas separadamente, adicione
# comentários de apóstofos simples ''' e ''' ENTRE um programa e outro.
# Exemplo abaixo:

'''
print('Programa X')
código

'''

print('Programa 01')

count = 0

while count != 5:
    # a linha abaixo resume o comando 'count = count + 1'
    count += 1
    # imprime 'count' a partir de 1 até 5
    print(count)
print('\n')


print('Programa 02')

count = 0

while count <= 20:
    # resume o comando 'count = count + 3'
    count += 3
    # imprime 'count' a partir de 3, somando + 3 
    print(count)
print('\n')

print('Programa 03')
# adicionamos o numero 20 a variavel
count = 20

while count >= 0:
    # count diminui -3 a cada número menor ou igual a 0
    # partindo de 20
    count -= 3
    print(count)
print('\n')