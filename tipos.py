# Tipo Primitivo
n1 = input('Digite um valor:\n')
print(type(n1))

# Tipo Inteiro
n2 = int(input("Didite outro valor\n"))
print(type(n2))

# Tipo Real ou Flutuante

n3 = float(input('Digite mais um valor:\n'))
print(type(n3))

# Tipo Boleano
n4 = bool(input('Digite outro:\n'))
print(type(n4))

# extras

# Quando usamos o isnumeric e não preenchemos o (), ele pergunta se o que foi digitado é um número ou não.
n5 = input('Digite algo:\n')
print('É um número?')
print(n5.isnumeric())
# Aqui pergunta se é uma letra, pois usamos o isalpha.
print('É uma letra?')
print(n5.isalpha())
# Usando o isaalnum, ele pergunta se é alfanumérioco.
print('É Alfanumérico?')
print(n5.isalnum())
#Usando o isupper, ele pergunta se está em letras maiúsculas.
print('Está em letras maiúsculas?')
print(n5.isupper())
# O islower é poara perguntar se está em minúsculo.
print('Está em minúsculo?')
print(n5.islower())
# Para saber se pode ser impresso usamos o isprintable.
print('Pode ser impresso?')
print(n5.isprintable())
# O isspace é para saber se é um espaço
print('É espasso?')
print(n5.isspace())

