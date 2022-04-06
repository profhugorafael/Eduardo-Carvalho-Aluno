#leio a quantidade de entradas
size = int(input())

#leio a linha com todos os dados juntos
line = input()

#atribua para a linha, a linha separano os elementos
line = line.split()

# DEBUG
# print(line)

#supor que o primeiro é o menor
posicao = 0
menor = int(line[0])

#para cada i começando em zero e menor que size
for i in range(size):
  #se for zero eu pulo
  if i == 0:
      continue
  if int(line[i]) < menor :
      menor = int(line[i])
      posicao = i

print(f'Menor valor: {menor}')  
print(f'Posicao: {posicao}')