# Desafio 14 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite seu salário: R$'))
aumento = salario * (15/100)
nvsalario = salario + aumento
print('Seu salário sem o aumento era de: R${} e com o aumento de 15% fica: R${}'.format(salario, nvsalario))