#conversao de dolar para real basica
dolar = 4.87
real = float(input('Insira a quantidade de dinheiro em reais que voce possui:'))
possivel_comprar = real / dolar
print('Com {} reais voce consegue comprar {:.2f} dolares'.format(real, possivel_comprar))