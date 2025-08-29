# Exercício Python 05: Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a = input('Digite um algo:')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços? {}'.format(a.isspace()))
print('É um número? {}' .format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanumérico? {}'.format(a.isalnum()))
print('Está em letras maiúsculas? {}'.format(a.isupper()))
print('Está em letras minúsculas? {}'.format(a.islower()))
print('Está capitalizada? {}'.format(a.istitle()))

