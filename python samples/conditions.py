nota1 = float(input())
nota2 = float(input())

media = (nota1 + nota2)/2.00

print(f'A media das notas foi {media:.2f}')

if (nota1 < 4) or (nota2 < 4) :
  print('Reprovado')
elif media >= 7.0  :
  print('Aprovado')
elif media >= 4.0:
  print('Recuperação')
else:
  print('Reprovado')