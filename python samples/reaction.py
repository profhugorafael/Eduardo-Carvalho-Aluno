pressao = 0

while True :

  if pressao > 15 : 
    print('a pressao atingiu limites fora do esperado!')
    break

  if (pressao < 4) or (pressao > 10) :
    print('ajustando a pressao')
    pressao += 1
    continue

  pressao += 1
  print('reação acontecendo')