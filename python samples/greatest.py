# entrada:
# 15
# 1 2 3 4 5 9 7 8 2 3 11 2 3 4 5
# saída:
# 11

#  -----------------

size = int(input('digite a quantidade de valores a serem lidos:'))

line = input() 
line = line.split()

print(line)

maior = int(line[0])

for i in range(size):

  if i == 0: 
    continue

  if int(line[i]) > maior :
    maior = int(line[i])

print(f'O maior é {maior}')
