# Exercício Python 05: Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n = input('Digite um algo:')
print('O tipo primitivo desse valor é', type(n))
print(n.isupper(), n.isnumeric(), n.isalnum())
