import datetime
ano_atual = datetime.date.today().year
print('Ano atual é {}.'.format(ano_atual))
ano = int(input('Insira um ano: '))
if (ano % 4) == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bissexto!')
else:
    print('Não é bissextto!')