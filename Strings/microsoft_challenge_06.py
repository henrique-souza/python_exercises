#caso queira executar os programas separadamente, 
# use três citaçções simples ''' na linha inicial e final ''' 
# de cada "# programa x"

#programa 01

primeira_string = 'Uma string literal'
segunda_string = "Uma string literal"
print(segunda_string == primeira_string) #irá imprimir um boolean: True

#programa 02

terceira_string = ('Uma única sequência literal citada com uma " citação dupla')
quarta_string = ("Duas sequências literais citadas com ' uma única citação")
print ('\n')
print(terceira_string)
print(quarta_string)

#programa 03

quinta_string = ('Uma sequência literal citada com uma \' unica citação escapada')
sexta_string = ("Uma sequência literal citada com uma \" citação dupla")
setima_string = ('Uma sequência literal com um \n caractere de linha')
oitava_string = ('Uma sequência literal com um \t caractere de guia ou tabulação')
print ('\n')
print(quinta_string)
print(sexta_string)
print(setima_string)
print(oitava_string)

#programa 04

nona_string = r"Uma sequência literal com uma \n nova linha impressa crua"
print ('\n')
print(nona_string)


#programa 05


decima_string = '''Uma sequência literal
em mais de uma linha
às vezes conhecida como cadeia de caracteres verbatim'''
# para executar o "#programa 06" sem interferencias dos dados da
# variavel "decima_string", favor adicionar comentários com 
# citações simples ''' ANTES e DEPOIS ''' dos dados.
decimaPrimeira_string = """Outra sequência literal
    em mais de uma linha
usando citação dupla"""
print ('\n')
print(decima_string)
print ('\n')
print(decimaPrimeira_string)


#programa 06

primeiroNome = 'Conrad'
segundoNome = 'Grant'
terceiroNome = 'Bob'
print ('\n')
print(primeiroNome, segundoNome)
print(primeiroNome, segundoNome, terceiroNome)
print(primeiroNome, segundoNome, terceiroNome, sep='-')
print(primeiroNome, segundoNome, terceiroNome, sep='-', end='.')
