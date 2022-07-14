numero = int(input('Ingrese un entero positivo: '))
primos = []

for i in range(2, 1000):
  primo = True
  for j in range(1, i+1):
    if (i%j == 0 and j!=1 and j!=i):
      primo = False
      continue
  if primo:
    primos.append(i)

divisores = []
numeroParcial = numero
i = 0

while numeroParcial > 1:
  if (numeroParcial%primos[i] == 0):
    numeroParcial = int(numeroParcial/primos[i])
    divisores.append(primos[i])
  else:
    i += 1

divisoresUnicos = []
i = 0
cantidad = 1

while i<len(divisores):
  if(len(divisores) == 1):
    divisoresUnicos.append(divisores[i])
    divisoresUnicos.append(cantidad)
    break
  else:
    if i == 0:
      divisoresUnicos.append(divisores[i])
    else:
      if divisores[i] == divisores[i-1]:
        cantidad += 1
      else:
        divisoresUnicos.append(cantidad)
        cantidad = 1
        divisoresUnicos.append(divisores[i])
      if i == len(divisores)-1:
        divisoresUnicos.append(cantidad)
    i += 1

listaDivisores = ''

for i in range(0, len(divisoresUnicos), 2):
  if (i == len(divisoresUnicos)-2):
    if len(divisoresUnicos) == 2:
      listaDivisores += str(divisoresUnicos[i])+' ('+str(divisoresUnicos[i+1])+')'
    else: 
      listaDivisores = listaDivisores[0:-2]
      listaDivisores += ' y '+str(divisoresUnicos[i])+' ('+str(divisoresUnicos[i+1])+')'
  else:
    listaDivisores += str(divisoresUnicos[i])+' ('+str(divisoresUnicos[i+1])+'), '

texto = 'Los divisores primos de {} son: {}'

print(texto.format(
  numero,
  listaDivisores
))