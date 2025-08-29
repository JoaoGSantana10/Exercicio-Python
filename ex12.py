# Exercício 12 - Faça um algoritmo que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
a = float(input('Digite a altura da parede:'))
l = float(input('Digite a largura da parede:'))
area = a * l
tinta = area / 2
print('A área da parede é: {}m², e a quantidade de tinta necessária para pinta-lá é: {}L'.format(area, tinta))
