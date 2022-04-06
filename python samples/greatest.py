# entrada:
# 15
# 1 2 3 4 5 9 7 8 2 3 11 2 3 4 5
# saída:
# 11

#entrada:
# 3
# 3 5 2
# saída
# 5
#  -----------------

# leio a quantidade de entradas
size = int(input('digite a quantidade de valores a serem lidos:'))

# leio a linha com todos os dados juntos
line = input() 

# atribua para a linha, a linha separando os elementos
line = line.split()
# line se torna um vetor de elementos

print(line)

# supor que o primeiro elemento é o maior
maior = int(line[0])

# para cada i começando em zero e menor que size
for i in range(size):

  # se for zero eu pulo
  if i == 0: 
    continue

  # caso o valor atual (line[i])
  # seja maior que meu suposto maior
  # a variável maior recebe o valor atual
  if int(line[i]) > maior :
    maior = int(line[i])

# apresento o maior valor depois de pesquisar na lista
print(f'O maior é {maior}')
