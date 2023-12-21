#conversor de Metros para Centrimetros e Milimetros
a = float(input('Digite um valor em metros:'))
cm= a * 100
mm = a / 1000

print('{:.2f} metros corresponde a {:.4f} centimetros e {:.4f} milimetros.'.format(a,cm, mm))