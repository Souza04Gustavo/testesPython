alt = float(input('Insira a altura da parede em metros:'))
comp = float(input('Insira o comprimento da parede em metros:'))
area = alt * comp
total_tinta = area / 2
print('Area total da parede: {:.2f}m²\nLitros de tintas necessarios: {:.2f}L'.format(area, total_tinta))