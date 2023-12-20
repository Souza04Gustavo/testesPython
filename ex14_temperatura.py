c = float(input('Temperatura em Celsius:'))
f = ((9*c)/5) + 32
print('{:.2f}°C equivalem a {:.2f}°F'.format(c, f))
f2 = float(input('Temperatura em Fahrenheit:'))
c2 = ((f - 32)*5)/9
print('{:.2f}°F equivalem a {:.2f}°C'.format(f2, c2))
