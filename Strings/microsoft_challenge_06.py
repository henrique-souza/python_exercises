'''
#programa 01

primeira_string = 'Uma string literal'
segunda_string = "Uma string literal"
print(segunda_string == primeira_string) #ira imprimir um True

#programa 02

terceira_string = ('Uma única sequência literal citada com uma " citação dupla')
quarta_string = ("Duas sequências literais citadas com ' uma única citação")
print(terceira_string)
print(quarta_string)

#programa 03

quinta_string = ('Uma sequência literal citada com uma \' unica citação escapada')
sexta_string = ("Uma sequência literal citada com uma \" citação dupla")
setima_string = ('Uma sequência literal com um \n caractere de linha')
oitava_string = ('Uma sequência literal com um \t caractere de guia ou tabulação')

print(quinta_string)
print(sexta_string)
print(setima_string)
print(oitava_string)

#programa 04
https://www.onlinegdb.com/#tab-stdin
nona_string = r"Uma sequência literal com uma \n nova linha impressa crua"
print(nona_string)

'''
#programa 05

decima_string = '''Uma sequência literal
em mais de uma linha
às vezes conhecida como cadeia de caracteres verbatim'''
decimaPrimeira_string = """Outra sequência literal
    em mais de uma linha
usando citação dupla"""

print(decima_string)
print ('\n')
print(decimaPrimeira_string)
