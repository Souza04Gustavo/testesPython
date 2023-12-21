#objetivo é mostrar as casas de um numero
#caminho matematico
num = int(input('Insira um numero entre 1 e 9999: '))
milhar = int(num/1000)
print('Milhar: {}'.format(milhar))
centena = int(num / 100) - (milhar*10)
print('Centena: {}'.format(centena))
dezena = int(num/10) - (milhar*100) - (centena*10)
print('Dezena: {}'.format(dezena))
unidade = num - (milhar*1000) - (centena*100) - (dezena*10)
print('Unidade: {}'.format(unidade))
#caminho string
palavra = str(input('Insira um numero entre 1 e 9999: '))
print('Milhar: {}'.format(palavra[0]))
print('Centena: {}'.format(palavra[1]))
print('Dezena: {}'.format(palavra[2]))
print('Unidade: {}'.format(palavra[3]))