# Formatando saídas de precisão

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

# Lendo mais de uma entrada na mesma linha

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

# `if` with resources
