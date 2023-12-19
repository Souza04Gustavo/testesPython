a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
s = a + b
m = a * b
d = a / b
di = a // b #divisao inteira
e = a ** b #exponenciação
re = a % b

print('A soma é {}, o produto é {} e a divisão é {:.2f}.'.format(s, m ,d), end=' ') #end='' é uma emenda de linha
print('Divisao inteira é {}, a potencia é {} e o resto da divisão é {}'.format(di, e, re))