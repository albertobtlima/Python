# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça tembém um programa que importe esse módulo e use algumas dessas funçoes.

import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'Aumentando R${preco} em 10%, temos R${moeda.aumentar(preco, 10)}')
print(f'Diminuindo R${preco} em 13%, temos R${moeda.diminuir(preco, 13)}')
