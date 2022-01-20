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
