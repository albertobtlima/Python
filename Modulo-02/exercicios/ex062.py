# Exercício 062
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# o programa encerra quando ele disser que quer mostra 0 termos.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Prograssão finalizada com {} termos mostrados.'.format(total))
