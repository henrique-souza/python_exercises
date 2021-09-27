import random # dar uma lida melhor quando chegar em casa

roll = 0
count = 0

while roll != 5:
  count = count + 1
  roll = random.randint(1, 5)
  print(roll)

print(f'It took {count} rolls to roll a 5!')
