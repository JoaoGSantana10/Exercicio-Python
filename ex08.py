nome = str(input('Qual o seu nome:'))
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m  = (n1 + n2) / 2
print('Olá {}, a média das suas nota é: {:.1f}'.format(nome, m))