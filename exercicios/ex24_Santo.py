#Verificar se a cidade comeca com Santo
cidade = str(input('Insira a cidade em que voce nasceu: ')).strip()
cidade_lista = cidade.upper().split()
print('SANTO' in cidade_lista[0])
#print(cidade[:5].upper() == 'SANTO')