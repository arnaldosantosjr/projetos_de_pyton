# A função desse programa é mostrar quanto o consumidor paragá ao receber 5% de desconto em um produto.

p = float(input('Digite o valor do produto\n'))
np = p - (p * 5/100)
print('Você irá pagar o valor de R$ {:.2f}'.format(np))
