print('Simple calculator!')

first_number = int(input('First number? '))

operation = input('Operation? ')

second_number = int(input('Second number? '))


if operation == '*':

    product = f'\nProduct of {first_number} * {second_number} equals {first_number * second_number}'
    print(product)
    exit()


print('\n')
