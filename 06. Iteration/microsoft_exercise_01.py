import random # dar uma lida melhor quando chegar em casa

roll = 0
count = 0

while roll != 5:
  count = count + 1 # count faz a conta de quantas vezes os números foram
  # sortidos até chegar o número 5
  roll = random.randint(1, 5) # sorteia os números de 1 a 5
  print(roll) # joga na tela os números de 1 a 5, até que apareça 5.

print(f'It took {count} rolls to roll a 5!')
