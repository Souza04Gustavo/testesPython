km = float(input('Total de KM''s rodados:'))
dias = int(input('Total de dias rodados:'))
preco = (dias * 60) + (0.15 * km)
print('Total a pagar: {:.2f}R$'.format(preco))