# Desafio 13 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o preço do produto: R$'))
d = p * (5/100)
np = p - d
print('O preço do produto sem o desconto é: R${} e com o desconto de 5% fica: R${}'.format(p, np))