
#função que coloca Hello na tela
def sayHello():
  print('hello')

#função que define a soma de 2 numeros inteiros
def soma(x, y):
  x = int(x)
  y = int(y)
  
  #retorna soma
  return x+y


#função que define taxa para calculo de juros
def calculaJuros( amount ):
  amount = float(amount)
  tax = 0.2

  #função que define taxa para calculo de juros
  return amount*tax


def montante ( capital ):
  return capital + calculaJuros(capital)

def menu():
  print('1 - say Hello')
  print('2 - calcula soma')
  print('3 - calcula montante')
  print('0 - sair do programa')

print('Seja bem vindo ao sistema')

menu()
option = input('digite uma opção do menu: ')

while option != '0' :
  print('------------------------')
  if option == '1':
    sayHello()

  elif option == '2':
    print('## SOMANDO ##')
    var1 = int(input('digite a primeira variável: '))
    var2 = int(input('digite a segunda variável: '))
    print(f'A soma é {soma(var1, var2)}')
  
  elif option == '3' :
    print('## CALCULANDO JUROS SOB CAPITAL ##')
    capital = float(input('digite o capital: '))
    print(f'O montante gerado pelo capital é {montante(capital)}')

  print('------------------------')

  menu()
  option = input('digite uma opção do menu: ')
  
  