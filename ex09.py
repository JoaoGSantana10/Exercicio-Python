# Exercício 09 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
v = float(input('Digite um valor em metros:'))
cm = v / 100
mm = v / 1000
print('O valor em metros é: {}m \n O valor em Cemtímetros é: {}cm \n O valor em Milímetros é: {}mm'.format(v, cm, mm ))
