# Aqui a pessoa sabera quanto receberá em seu novo salário após o justede de 15%

s = float(input('Qual o valor do seu selário atual?\n'))
ns = s + (s*15/100)
print('Seu novo salário é R$ {:.2f}'.format(ns))