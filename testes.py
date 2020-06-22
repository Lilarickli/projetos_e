n = int(input('Digite um numero: '))
divisores = 0

for divisor in range(1, n + 1):
    if n % divisor == 0:
       divisores += 1

if divisores == 2:
    print(n, 'é primo')
else:
    print(n, 'não é primo')