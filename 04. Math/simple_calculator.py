print('Simple calculator!')

first_number = input('First number? ')

operation = input('Operation? ')

if not operation.isalnum() == False: # infelzimente essa função não consegue ler espaços em branco, e fecha o programa depois do segundo número
    print('Operation not recognized.')
    exit()

second_number = input('Second number? ')

if first_number.isnumeric() == False or second_number.isnumeric() == False:
    print('\nPlease input a number.')
    exit()

first_number = int(first_number)
second_number = int(second_number)

if operation == '*':

    product = f'\nProduct of {first_number} * {second_number} equals {first_number * second_number}'
    print(product)

elif operation == '-':
    difference = f'\nDifference of {first_number} - {second_number} equals {first_number - second_number}'
    print(difference)

elif operation == '+':
    sum = f'\nSum of {first_number} + {second_number} equals {first_number + second_number}'
    print(sum)

elif operation == '/':
    quotient = f'\nQuotient of {first_number} / {second_number} equals {first_number / second_number}'
    print(quotient)

elif operation == '%':
    modulus = f'\nModulus of {first_number} and {second_number} equals {first_number % second_number}'
    print(modulus)

elif operation == '**':
    exponent = f'\nExponent of {first_number} and {second_number} equals {first_number ** second_number}'
    print(exponent)
    exit()

'''
RESOLUÇÃO DA MICROSOFT 

print('Simple calculator!')

first_number = input('First number? ')

if first_number.isnumeric() == False:
    print('Please input a number.')
    exit()

operation = input('Operation? ')

second_number = input('Second number? ')

if second_number.isnumeric() == False:
    print('Please input a number.')
    exit()

first_number = int(first_number)
second_number = int(second_number)

result = 0
if operation == '+':
    result = first_number + second_number
    label = 'sum'
elif operation == '-':
    result = first_number - second_number
    label = 'difference'
elif operation == '*':
    result = first_number * second_number
    label = 'product'
elif operation == '/':
    result = first_number / second_number
    label = 'quotient'
elif operation == '**':
    result = first_number ** second_number
    label = 'exponent'
elif operation == '%':
    result = first_number % second_number
    label = 'modulus'
else:
    print('Operation not recognized.')
    exit()

print(label + ' of ' + str(first_number) + ' ' + operation + ' ' + str(second_number) + ' equals ' + str(result))

'''