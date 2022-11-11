"""Recebe uma linha de números aleatórios e retorna um gráfico"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import collections

# Prob de Menina = Prob de Menino = 1/2 ou 0,5 - Menina é 0 e Menino é 1
# meninas <0.5
# meninos >=0.5

# n10           recebe valores das linhas 0 a 9
# n100          recebe valores das linhas 0 a 99
# n1000         recebe valores das linhas 0 a 999
# n10000        recebe valores das linhas 0 a 9999
pd.options.display.float_format = '{:,.1f}'.format

coluna = [0]
linha = range(10000)
dados = np.round(np.random.random(10000), 1) # randomiza de 0 a 1
tabela = pd.DataFrame(data=dados, index=linha, columns=coluna)

# retorna True se os valores contidos no "[indice 0 a 9, coluna]" forem maiores que 0,5
n10_meninas = 0.5 < tabela.iloc[0:9, 0]

# retorna True se os valores contidos no "[indice 0 a 9, coluna]" forem menores ou iguais a 0,5
n10_meninos = 0.5 >= tabela.iloc[0:9, 0]

# retorna True se os valores contidos no "[indice 0 a 99, coluna]" forem maiores que 0,5

print(f'{sum(n10_meninas)} MENINAS foram localizadas num range de 10 registros.')
print(f'{sum(n10_meninos)} MENINOS foram localizadas num range de 10 registros.')

# print(tabela.values[9])
# print(tabela.loc[0:9, 0].count(0,5))

# print(tabela.loc[tabela['Species'] == 'Iris-setosa'].count())

# print(tabela.iloc[0:9])

# # creating the dataset
# data = {'%10': 20, '%100': 15, '%1000': 30, '%10000': 35}
# courses = list(data.keys())
# values = list(data.values())
#
# fig = plt.figure(figsize=(10, 5))
#
# # creating the bar plot
# plt.bar(courses, values, color='blue', width=0.4)
#
# plt.xlabel("aaaaaaaaa")
# plt.ylabel("bbbbbbbbbbbb")
# plt.title("Probabilidade de nascimento de Meninos ou Meninas")
# plt.show()
