# Linguagens Compiladas

Basicamente, são escritas de forma não ambígua e com regras bem **estabelecidas**, de modo que possam ser traduzidas para uma máquina executar depois.

## Vantagens

- Mais rápida

## Desvantagens

- Não necessariamente será portátil

# Linguagens Interpretadas

São dinamicamente traduzidas para comandos na máquina, sem passar pelo baixo nível.

## Vantagens

- Alta portabilida e facilidade de escrita

## Desvantagens 

- Mais lenta

# Princípios Básicos da Programação

## 1. Saída de dados

`pyhton`:
```py
 print("Hello World")
```

`C++`:
```c++
  // input and output stream
  #include <iostream> 

  // coloco no modo standard
  using namespace std;

  // crio meu entrypoint
  int main(){

    cout << "Hello World!" << endl;
    // command out
    // endline

    return 0;
    // forço a parada do programa
  }
```

### Interpolação no print

```py
a = 2
print(f'O valor de é {a}')
```

## 2. Variáveis

Tipos mais usuais de variáveis: 

|Nome|Keyword|Objetivo|
|:---:|:---:|:---:|
|Inteiro|`int`| Números inteiros |
|Real|`float`|Número com *ponto flutuante*|
|Caracter|`char`| Um caracter |
|String|`str`| É um conjunto de caracteres (*vetor*)|

## 3. Entrada e Saída de dados

```py
frase = input()
print(frase)
```

### fazendo uma entrada melhor:
```py
frase = input('Digite uma frase: ')
print(frase)
```

### casting de entrada
Aviso de tipo a ser recebido ou lido:

> Se o o `input()`  do `a` for `2` pelo terminal, ele será da classe das strings(`str`)

> Se fizermos `int(input())` do `a` for `2` pelo terminal, ele será da classe inteiro(`int`)

```py
a = input('digite o valor da variável a: ')
b = int(input('digite o valor da variável b: '))

print(int(a)+b)
```

### Keyword `type()`

Retorna o tipo(classe) a qual essa variável pertence.

código:
```py
  a = input();
  print( type(a) )
```