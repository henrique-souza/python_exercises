# caso queira testar os programas separadamente, adicione
# comentários de apóstofos simples ''' e ''' ENTRE um programa e outro.
# Exemplo abaixo:
'''

print('Programa X')
código

'''


print('Programa 01\n')

mensagem = str.capitalize('primeira mensagem')
print(mensagem)

mensagem = 'segunda mensagem'.capitalize()
print(mensagem)

mensagem = 'terceira mensagem'
print(mensagem.capitalize())
print('\n')


print('Programa 02\n')

mensagem2 = 'ola mundo'
print(mensagem2.lower())
print(mensagem2.upper())

mensagem2 = mensagem2.title()
print(mensagem2)
print(mensagem2.swapcase())
print('\n')

print('Programa 03\n')

localizacao = 'Mississipi'
print(localizacao.count('s'))
print('\n')

print('Programa 04\n')

print(len('Quantos caracteres tem nesta cadeia de caracteres?'))
print('\n')

print('Programa 05\n')

mensagem3 = 'racecar'
print(mensagem3.startswith('r'))
print(mensagem3.startswith('a'))
print(mensagem3.startswith('ra'))

print(mensagem3.endswith('r'))
print(mensagem3.endswith('a'))
print(mensagem3.endswith('ar'))  # estes comandos irão retornar se
# a informação passada no parametro é True ou False
print('\n')

print('Programa 06\n')

mensagem4 = 'A raposa marrom, que é rápida, pula sobre o cão preguiçoso'

print(mensagem4.find('o'))
# método find() informa a localização da cadeia de caracteres
# por exemplo, ele acha o primeiro 'o' e imprime a localização
# do mesmo, dentro da cadeia de caracteres, sendo A posicionado em 0,
# a letra 'o' seria posição 5
print(mensagem4.find('a'))
print(mensagem4.find('A'))
print(mensagem4.find('ã'))
print(mensagem4.find(','))
print('\n')

print('Programa 07\n')

mensagem5 = '     meio     '
# faz com que espaços da esquerda sejam ignorados
print('.' + mensagem5.lstrip() + '.')
# faz com que espaços da direita sejam ignorados
print('.' + mensagem5.rstrip() + '.')
# faz com que todos espaços sejam ignorados
print('.' + mensagem5.strip() + '.')
print('\n')

print('Programa 08\n')

mensagem6 = 'Brevidade é a essência da sagacidade'
mensagem6 = mensagem6.replace('essência', 'alma')
# método replace() subistutui palavras de uma cadeia de caracteres
print(mensagem6)
print('\n')


print('Programa 09\n')

mensagem7 = 'Henrique'
print(mensagem7.rjust(20))
print(mensagem7.rjust(20, '-'))
print(mensagem7.ljust(20))
print(mensagem7.ljust(20, '-'))
print('\n')
