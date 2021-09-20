# caso queira testar os programas separadamente, adicione
# comentários de apóstofos simples ''' e ''' ENTRE um programa e outro.
# Exemplo abaixo:
'''

print('Programa X')
código

'''

first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value = first_value.rjust(31)
first_value = first_value.title()
print(first_value)

# Second challenge
second_value = second_value.replace('-', ' ')
second_value = second_value.strip()
second_value = second_value.capitalize()
print(second_value)

# Third challenge
third_value = third_value.lower()
third_value = third_value.replace(' ', '')
third_value = third_value.strip()
third_value = third_value.capitalize()
third_value = third_value.rjust(30)
third_value = third_value.replace('-', ' ')
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)

print(fourth_value, fifth_value, sixth_value, sep='#', end='!\n')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.

print(f'{fourth_value:^22}\n'
f'{fifth_value:^22}\n'
f'{sixth_value:^22}')

''' Resultados que o desafio está pedindo abaixo: 

       First Challenge        
Second challenge
               Third challenge
fourth#fifth#sixth!
        fourth
        fifth
        sixth
'''

'''
PT - Soluções sugeridas pela Microsoft: 
EN - Soluctions proposed by Microsoft:

# First challenge
first_value = first_value.strip()
first_value = first_value.lower()
first_value = first_value.title()
first_value = f'{first_value:^30}'

# Second challenge
second_value = second_value.replace('-', '')
second_value = second_value.strip()
second_value = second_value.capitalize()

# Third challenge
third_value = third_value.replace(' ', '')
third_value = third_value.replace('-', ' ')
third_value = third_value.swapcase()
third_value = f'{third_value:>30}'

print(first_value)
print(second_value)
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#', end='!')

# Fifth challenge - use only a single print() function. Create tabs and new lines using f-strings.
print(f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')
'''
