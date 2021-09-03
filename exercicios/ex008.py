#O programa converte o valor dado em metros para centímetroe e milimetros

m = int(input('Digite um valor para conversão.\n'))
cm = m * (10**2)
mm = m * (10**3)
print('{}m vale {}cm ou {}mm.'.format(m, cm, mm))
