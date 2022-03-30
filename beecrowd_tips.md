# 📍Comentários no código

Comentários são essenciais para um código limpo e que possa ser facilmente entendido por outros programadores ou por você próprio no futuro. Bons comentários explicam de forma eficiente o que está sendo feito nas linhas ou em um determinado bloco de comando.

> Comentários são completamente ignorados durante a interpretação do código pela máquina, o objetivo dos comentários é ajudar os desenvolvedores.

## 1. Como criar comentários

Para criar comentários em apenas uma linha usamos a `#` e tudo que está após ela é ignorado.

```py
  # imprimindo Hello World
  print('Hello World') # imprimindo
  #Hello World
```

O atalho que transforma o conteúdo de uma linha em comentário ou inicia um comentário no Visual Studio Code é `ctrl` + `;`

Outra maneira que podemos usar são os comentários delimitados, isto é, que podem ser uma parte de uma linha ou até multi-linhas. Usamos o `"""` para abrir e para fechar.

```py
"""
  Este comentário é delimitado
  e permite que várias linhas sejam comentadas
  no intervalo delimitado pelas 3 aspas duplas
"""
print('Hello World')
```

## 2. Como criar **bons comentários**

Bons comentários são apenas convenções já percebidas com a experiência, não adianta fazer um comentário que seja dificil de interpretar, pois isso só atrapalha a leitura do código.

### ❌ Um exemplo Ruim
```py
# Testando a seleção da variável inteira e verificando
if a > 2: # se ela for maior que 2 eu realizo o código interno
  # sendo maior que 2 eu imprimo
  # que ela é maior que 2
  print('é maior que 2')
```

### ⚠️ Pontos negativos:
1. Ausência de palavras-chave(***Keywords***)
2. Muitas ideias repetidas e não resumidas
3. Falta de uma padronização no estilo, escolha comentar nas laterais, na linha acima, ou na linha abaixo, mas mesclar estilos confunde a leitura.

### ✅ Melhorando:

```py
# Caso a variável seja maior que 2
if a > 2:

  # Imprimo um feedback
  print('é maior que 2')
```

ou

```py
if a > 2: # Se a for maior que 2
  print('é maior que 2') # Imprimo que é maior
```

Além destes, pode-se usar comentários em multi-linhas para identificar dados do projeto, como nome, data, e nome.

```py
"""
  Name: Just comment project
  Author: Hugo Rafael
  Date: March 30, 2022
"""
print("Awesome project :)")
```


# 📍 Formatando saídas de precisão

Para formatarmos saídas de precisão em python usaremos um comando dentro do modo de formatação do print.

Imprimindo saída interpolada sem formatação:

```py
nota = 7.5
nome = "Joao da Silva"
print(f'O nome do aluno é {nome} e sua nota é {nota}')
```

Caso nosso objetivo fosse com que a nota saísse sempre com duas casas decimais de precisão, podemos formatar a saída através de **expressões regulares** colocadas ao lado da variável indicadas por `:`.

Exemplo, para formatarmos um número para um modelo `float`, com ponto flutuante, e especificamente com 3 casas decimais após a vírgula.

```py
nota = 7.5
nome = "Joao da Silva"
print(f'O nome do aluno é {nome} e sua nota é {nota:.3f}')
```

Desta forma, indicamos através da expressão regular `.3f` que queremos 3 casas depois do ponto flutuante naquela variável.

# 📍Lendo mais de uma entrada na mesma linha

Nem sempre os problemas estarão da melhor maneira para serem lidos em python, já que o python faz a **inferência de tipo** como *string*(`str`). Por isso teremos dificuldade de ler entradas do tipo:

Problema: Mostre a soma de dois números.

Caso de entrada:
```
2 3
```

Se lermos do jeito tradicional:
```py
a = input()
b = input()
```

Este código não é capaz de interpretar um código que entra em apenas uma linha. Para ler isto o python usa o método `split()` que como o nome sugere, parte esses dados em um conjunto de dados menores do tipo: 

```
'2 3' --------> ['2' , '3']
```

Dessa forma com os elementos separados conseguimos acessá-los individualmente na forma de um vetor(*array*).

<!-- # `if` with resources -->
