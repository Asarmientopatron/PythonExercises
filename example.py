num = int(input('Digite un número entero: '))
primo = True

for i in range(1,num+1):
  if (num%i == 0 and i != num and i != 1) :
    primo = False
    break

response1 = "{} NO es un número primo"
response2 = "{} es un número primo"

if primo:
  print(response2.format(num))
else:
  print(response1.format(num))
