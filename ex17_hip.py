import math
ca = float(input('Cateto adjacente: '))
co = float(input('Cateto oposto: '))
hip = math.hypot(ca, co)
print('Hipotenusa: {:.3f}'.format(hip))