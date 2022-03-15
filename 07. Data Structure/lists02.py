from ast import For
import random

print('Programa 01\n')

numbers = [1, 3, 5]

# irá retornar um true
print(5 in numbers)
# irá retornar um false
print(8 in numbers)

# irá retornar um false
print(5 not in numbers)
# irá retornar um true
print(8 not in numbers)

print('\n')

print('Programa 02\n')

cidades = ["Belford Roxo", "Duque de Caxias", "Nova Iguaçu"]

for cidade in cidades:
    print(cidade)

print('\n')

print('Programa 03\n')

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
numbers.sort()

for number in numbers:
    if number > 42:
        break
    print(number)

print('\n')

print('Programa 04\n')

numbers = []

while len(numbers) < 5:
    numbers.append(random.randint(1, 100))

for number in numbers:
    print(number)
    if number >= 90:
        print('Achei um número maior que 90')
        break
else:
    print('Não achei um número maior que 90.')

print('Finalizado.')

print('\n')

print('Programa 05\n')

valores = ["notebook", 7, "telefone", 3, "dslr", 5]
equipamento = []

# A lista tem valores int, mas queremos
# imprimir apenas as strings

for valor in valores:
    if isinstance(valor, str) == False:
        continue
    equipamento.append(valor)
# Se o print abaixo estivesse indentado no laço for
# ele imprimirá os dados str um por um, até o
# resultado final.
print(equipamento)

print('\n')
