# Exercício 11 - Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$ 5,00
n = float(input('Digite o quanto de dinheiro que vocẽ tem na carteira R$:'))
d = n / 5.00
print('Com R${:.2f} você pode comprar U${:.2f}'.format(n, d))
