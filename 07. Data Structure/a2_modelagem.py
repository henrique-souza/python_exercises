# Prob de Menina = Prob de Menino = 1/2 ou 0,5 - Menina é 0 e Menino é 1
# Exercicio 01
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

coluna = range(1)
linha = range(10001)
dados = np.random.random(10001)
tabela = pd.DataFrame(data=dados, index=linha, columns=coluna)


# creating the dataset
data = {'%10': 20, '%100': 15, '%1000': 30,
        '%10000': 35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(courses, values, color='blue',
        width=0.4)

plt.xlabel("aaaaaaaaa")
plt.ylabel("bbbbbbbbbbbb")
plt.title("Probabilidade de nascimento de Meninos ou Meninas")
plt.show()
