# Estruturas de repetição

Aqui nosso objetivo não é apenas interagir e verificar uma determinado condição, mas sim iterar por ela ou por algum intervalo.

# Estrutura `while` - *enquanto*

```py
while condição  :
  # seu codigo
```

O while executa enquanto a condição for verdadeira, logo é preciso também inserir alguma atualização ou condição de parada.

Exemplo: Loja que enquanto sem estoque compra até zerar e enquanto com estoque vende até zerar.

```py
estoque = 10

while estoque != 0 :
  if estoque > 0 :
    print(f'vendendo... || estoque = {estoque} ')
    estoque -= 1
  else:
    print(f'comprando... || estoque = {estoque} ')
    estoque += 1
```

## 3 Elementos essenciais para repetições

1. Inicialização.
2. Verificação.
3. Atualização.

# *Keywords* das estruturas de repetição

## 1. `break`

Interrompe o laço de repetição e interrompe a estrutura também, cortando a execução e retornando ao escopo normal.

```py
while True :
  if estoque == 10 : break
  estoque+=1

print('fim do programa')
```

## 2. `continue`

Interrompe o laço e pula para o próximo. Mantém o loop acontecendo ainda.

```py
pressao = 0

while True :

  if pressao > 15 : 
    print('a pressao atingiu limites fora do esperado!')
    break

  if (pressao < 4) and (pressao > 10) :
    print('ajustando a pressao')
    pressao += 1
    continue

  pressao += 1
  print('reação acontecendo')

```

## 3. `pass`

A `pass` permite que eu pule determinadas implementações durante meu código.

# `for` - *para*

Exemplo:
```py
frase = 'cada palavra da sequencia'
sequencia = frase.split()

for expressao in sequencia:
  print(expressao)
```

## `for` iterativo

Serve muito bem para manipular elementos em sequencias, vetores ou `strings`.

Outros exemplos:

```py
palavra = 'teste'

for char in palavra:
  print(char)
```

saída:
``` 
t
e
s
t
e
```

## `for` + `range`

fazendo com `while`:
```py
i = 0

while i <= 10 :
  print(i)
  i += 1
```

melhorando com `for` + `range`:
```py
for i in range(4):
  print(i)
```

saída:
```
0
1
2
3
```

## Como funciona a range

A `range` é uma função com **overload** de parâmetro

1. `range(stop)` equivalente a `range(0, stop, 1)`
2. `range(start, stop)` equivalente a `range(start, stop, 1)`
3. `range(start, stop, step)`