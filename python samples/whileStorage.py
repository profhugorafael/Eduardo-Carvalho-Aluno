estoque = int(input('Digite o valor do estoque: '))

while estoque != 0 :
  if estoque > 0 :
    print(f'vendendo... || estoque = {estoque} ')
    estoque -= 1
  else:
    print(f'comprando... || estoque = {estoque} ')
    estoque += 1

print('O estoque terminou!')