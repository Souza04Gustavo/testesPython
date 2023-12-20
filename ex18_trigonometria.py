import math
ang = float(input('Insira um angulo: '))
ang_rad = math.radians(ang)
print('Sen({}): {:.2f}'.format(ang, math.sin(ang_rad)))
print('Cos({}): {:.2f}'.format(ang, math.cos(ang_rad)))
print('Tan({}): {:.2f}'.format(ang, math.tan(ang_rad)))