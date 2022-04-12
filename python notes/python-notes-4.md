# Funções

Funções são essenciais para que possamos usar o princípio do `reuso` em nossos códigos.

## Exemplo de uma função simples

```py
def say( message ) :
  print(message)

say('something')
```
output:
```
something
```

# Keywords no uso das funções

# 1. **`def`**

`def` é o gatilho para avisarmos que iremos criar uma função, logo ao lado da `def` colocamos o nome que iremos utilizar para esta função.

```py
def <nome da função> ...
```

# 2. Parametros da função

Para criar uma função podemos ou não colocar valores de entrada, como dados a serem usados internamente.

Exemplo sem parametros:
```py
def my_function ( ) :
  ...
```

Exemplo sem parametros:
```py
def my_function(parametro1, parametro2) :
```

## 3. Escopo

Um escopo é um bloco de código que está contigo dentro de alguma das expressões que aprendemos. Por exemplo, *dentro* do if, através da **indentração** do código.

```py
#fora o escopo

if condicao == True :
  #inicio do escopo
  #código aqui
  #fim do escopo

#fora o escopo
```

## 4. **`return`**

A `return` serve para entregarmos um resultado depois de utilizarmos a função.

Exemplos:

```py
def soma(x, y):
  return x + y

def jurosSelic(quantia):
  taxa = 10.15
  return quantia*taxa

def menu():
  print('1 - calcular a soma')
  print('2 - calcular o juros')
  print('0 - sair do programa')
```

```py
#criando a media
def media(a, b):
  # passando os valores para inteiro
  a = float(a)
  b = float(b)

  # devolvo/retorno com o resultado
  return (a+b)/2.0

print( media(2.0, 3.0) )
```