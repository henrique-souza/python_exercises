# caso queira testar os programas separadamente, adicione
# comentários de apóstofos simples ''' e ''' ENTRE um programa e outro.
# Exemplo abaixo:

'''
print('Programa X')
código

'''

print('Programa 01')

valor_numerico = '7'
print(valor_numerico.isnumeric())

valor_string = 'Henrique'
print(valor_string.isnumeric())
print('\n')


print('Programa 02')

primeiro_valor = input('Primeiro numero: ')
segundo_valor = input('Segundo numero: ')

if primeiro_valor.isnumeric() == False or segundo_valor.isnumeric() == False:
    print('O valor digitado não é um número.')
    exit()
    
primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

soma = primeiro_valor + segundo_valor
print('Soma dos valores: ' + str(soma))
print('\n')
