print('Simple calculator!')

first_number = input('First number? ')

operation = input('Operation? ')

second_number = input('Second number? ')

if first_number.isnumeric() == False or second_number.isnumeric() == False:
    print('\nPlease input a number.')
    exit()

first_number = int(first_number)
second_number = int(second_number)

'''if operation.isinstance() == False:
    print('Operation not recognized.')
    exit()'''

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

print('\n')
