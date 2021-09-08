# Esse progrma consiste em converter o real em dólar americano
# No momento da criação desse código, o dólar estava custando R$ 5,32.

r = float(input('Digite quanto você tem na carteira.\n'))
d = r / 5.32
print('Com esse dinheiro você pode comprar US$ {:.2f} dólares'.format(d))