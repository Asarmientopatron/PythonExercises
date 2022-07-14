number = int(input('Ingrese un número entero positivo: '))
count = 0

for i in range(1, number+1):
  if number%i == 0:
    count += 1
  if count > 2:
    break

if count > 2:
  print('El número ingresado No es primo')
else:
  print('El número ingresado es primo')

