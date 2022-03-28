# Estruturas de Seleção (`if-elif-else`)

Executam ou não blocos de código.

> Similar ao antigo `goto:`

Exemplo: Aprovado > 7 e o resto reprovado
```py
nota = 7.3

if nota > 7 :
  print('Aprovado')
else:
  print('Reprovado')
```

```
Se <condição> :
  faça isso
Senão:
 faça isso 2
```

## Keyword `if`

Recebe uma expressão e checa se é verdadeira ou falsa. Executa o código interno se for verdadeira.

## Keyword `else`

Executa se a condição de um `if` previamente criado for falsa.

Exemplo: Aprovado >= 7 , recuperação nota>=4 e nota<7 e o9 resto reprovado.

```py
if nota >= 7 :
  print('Aprovado')
else:
  if nota >= 4:
    print('Recuperação')
  else:
    print('Reprovado')
```

Melhorando este código.

## Keyword `elif` (*else if*)

Melhoria do `else` que chama um `if` interno.

```py
if nota >= 7 :
  print('Aprovado')
elif nota >= 4:
  print('Recuperação')
else:
  print('Reprovado')
```

**observação:** posso ter quantos `elif`'s forem necessários.

# Operadores lógicos

## Operadores de igualdade

|Operador| Simbologia |
|:-:|:-:|
|Igual|`==`|
|Maior ou igual|`>=`|
|Menor ou igual| `<=` |
|Diferente| `!=` |


## Operador `and` - `&&`

Necessita que as duas condições sejam verdade para que seja verdade. Similar a intersecção de conjuntos, um elemento deve estar em ambos os conjuntos para que seja verdade o fato de estar na intersecção.

Compare com uma associação de chaves em série, se uma delas estiver fechada(*true*), porém a outra não estiver(*false*) a corrente não passa, ou seja *false*. O único caso que ambas as correntes passam é as duas chaves estando fechadas.

![and circuit](.\images\andcircuit.jpg)

result = `A && B`
|A|B|result = `A && B`|
|:--:|:--:|:---:|
|True|True|True|
|False|True| False|
|True|False| False|
|False|False| False |

## Operador `or` - `||`

Necessita que apenas uma das condições seja verdade para que seja verdade. Similar a união de dois conjuntos, que para pertencer a união, deve-se estar no mínimo em um dos conjuntos.

Análogo a associação de chaves em paralelo.

![or circuit](.\images\orcircuit.jpg)

result = `A || B`
|A | B |result|
|:--:| :--:|:---:|
|True|True| True|
|False|True| True |
|True|False| True|
|False|False| False |

## Operador `xor` - `^`

Este aqui é o operador **ou exclusivo**, isto é, caso as duas condições sejam verdadeiras, ele irá retornar falso, porém se apenas uma delas for verdadeira, ele retorna verdadeiro.

> Similar a expressão "ou ... ou ..." do português.

result = `A || B`
|A | B |result|
|:--:| :--:|:---:|
|True|True| True|
|False|True| True |
|True|False| True|
|False|False| False |


## Operador mod - `%`

Basicamente `a%b` retorna o resto de a dividido por b.

## Operador potências - `**`

`a**b` indica a elevado a b.

