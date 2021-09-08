# Nesse programa você vai ver quanto mede a área de uma parede e quantos litros de tinta será preciso para
# pintá-la sabendo que 1l de tinta pinta 2m².

b = float(input('Quantos metros mede a base?\n'))
h = float(input('Quanto mede a altura?\n'))
a = b * h
l = a / 2
print('A área a ser pintade é {}m²'.format(a))
print('Você precisará de {}l de tinta para pintar toda a parede'.format(l))

