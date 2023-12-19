#calculará 5% de desconto em qualquer produto
produto = float(input('Insira o valor:'))
valor_final = produto * 0.95
print('Com 5% de desconto o produto passa de {} para {:.2f} reais, tendo {:.2f} reais de desconto.'.format(produto, valor_final, produto*0.05))