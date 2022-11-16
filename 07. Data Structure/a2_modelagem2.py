"""Recebe uma linha de números aleatórios e retorna um gráfico"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

coluna = [0]
linha = range(10000)
dados = np.random.randint(1, 10, 10000)  # randomiza entre 1 e 10
tabela = pd.DataFrame(data=dados, index=linha, columns=coluna)

# nascer menina = 1, 2, 3, 4, 5, 6, 7
# nascer menino = 8, 9, 10

# retorna True se os valores contidos no "[indice 0 a 10, coluna]" forem menores ou iguais a 7
n10_meninas = 7 <= tabela.iloc[0:10, 0]

# retorna True se os valores contidos no "[indice 0 a 10, coluna]" forem maiores ou iguais a 8
n10_meninos = 8 >= tabela.iloc[0:10, 0]

# retorna True se os valores contidos no "[indice 0 a 100, coluna]" forem menores ou iguais a 7
n100_meninas = 7 <= tabela.iloc[0:100, 0]

# retorna True se os valores contidos no "[indice 0 a 100, coluna]" forem maiores ou iguais a 8
n100_meninos = 8 >= tabela.iloc[0:100, 0]

# retorna True se os valores contidos no "[indice 0 a 1000, coluna]" forem menores ou iguais a 7
n1000_meninas = 7 <= tabela.iloc[0:1000, 0]

# retorna True se os valores contidos no "[indice 0 a 1000, coluna]" forem maiores ou iguais a 8
n1000_meninos = 8 >= tabela.iloc[0:1000, 0]

# retorna True se os valores contidos no "[indice 0 a 10000, coluna]" forem menores ou iguais a 7
n10000_meninas = 7 <= tabela.iloc[0:10000, 0]

# retorna True se os valores contidos no "[indice 0 a 10000, coluna]" forem maiores ou iguais a 8
n10000_meninos = 8 >= tabela.iloc[0:10000, 0]

print(f'Existem {sum(n10_meninas)} MENINAS no range de {n10_meninas.count()} registros. \n '
      f'Existem {sum(n10_meninos)} MENINOS no range de {n10_meninos.count()} registros. \n\n'
      f'Existem {sum(n100_meninas)} MENINAS no range de {n100_meninas.count()} registros.\n'
      f'Existem {sum(n100_meninos)} MENINOS no range de {n100_meninos.count()} registros.\n\n'
      f'Existem {sum(n1000_meninas)} MENINAS no range de {n1000_meninas.count()} registros.\n'
      f'Existem {sum(n1000_meninos)} MENINOS no range de {n1000_meninos.count()} registros.\n\n'
      f'Existem {sum(n10000_meninas)} MENINAS no range de {n10000_meninas.count()} registros.\n'
      f'Existem {sum(n10000_meninos)} MENINOS no range de {n10000_meninos.count()} registros.')

# 10%
fn10_meninas = sum((n10_meninas * 100) / n10_meninas.count())
fn10_meninos = sum((n10_meninos * 100) / n10_meninos.count())

# 100%
fn100_meninas = sum((n100_meninas * 100) / n100_meninas.count())
fn100_meninos = sum((n100_meninos * 100) / n100_meninos.count())

# 1000%
fn1000_meninas = sum((n1000_meninas * 100) / n1000_meninas.count())
fn1000_meninos = sum((n1000_meninos * 100) / n1000_meninos.count())

# 10000%
fn10000_meninas = sum((n10000_meninas * 100) / n10000_meninas.count())
fn10000_meninos = sum((n10000_meninos * 100) / n10000_meninos.count())

X = ['%10', '%100', '%1000', '%10000']
Ygirls = [fn10_meninas, fn100_meninas, fn1000_meninas, fn10000_meninas]
Zboys = [fn10_meninos, fn100_meninos, fn1000_meninos, fn10000_meninos]

X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, Ygirls, 0.4, label='Meninas', color='red')
plt.bar(X_axis + 0.2, Zboys, 0.4, label='Meninos', color='blue')

plt.xticks(X_axis, X)
plt.xlabel("Parcela calculada")
plt.ylabel("Porcentagem")
plt.title("Simulação do nascimento de 10 mil meninas ou meninos")
plt.legend()
plt.show()
