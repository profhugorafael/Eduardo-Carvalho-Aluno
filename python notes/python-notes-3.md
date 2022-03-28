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
while estoque != 0 :
  if estoque > 0 :
    print(f'vendendo... || estoque = {estoque} ')
    estoque
  else:
    print(f'comprando... || estoque = {estoque} ')
```