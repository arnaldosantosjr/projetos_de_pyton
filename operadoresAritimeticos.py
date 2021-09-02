# Esse programa consisste em fazer operações aritméticas entre números.
# Usaremos o + para adição;
# Usaremos o - para subtração;
# Usaremos o * para multiplicação;
# Usaremos o / para divisão;
# Usaremos ** para potência;
# Usaremos // para divisão inteira;
# Usaremos  % para resto da divisão ( Ou módulo).
n1= int(input('Digite um valor:\n'))
n2= int(input('Digite outro valor:\n'))
sm= n1 +n2
sub = n1 - n2
pr = n1 * n2
div = n1 /n2
print('A soma entre esses valores é {}, a subtração é {}, o produto é {}, e a divisão é {:.3f}.'.format(sm, sub, pr, div))
pot = n1 ** n2
dvi = n1//n2
rd = n1 % n2
print('A potência de {} elevado a {} é {}, a divisão inteira é {}, e o resto ou módulo é {}.'.format(n1, n2, pot, dvi, rd))