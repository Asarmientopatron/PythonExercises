mat = [
  [1, 2, 3], 
  ['Avión', 'Bombilla', 'Corazón'],
]

for i in mat: # Esta es la forma más sencilla de acceder a cada posición individual de una lista de listas
  # print(i)
  for j in i:
    print(j)

# El for interno no necesariamente debe recorrer todas las columnas de la fila respectiva. Puede usarse para otros propósitos

print(len(mat)) # cantidad de filas
print(len(mat[0])) # cantidad de columnas en la fila 0

# Las listas de listas se recorren primero por fila y luego por columna.
# En el ejemplo anterior, la primera fila está compuesta por números, mientras que la segunda, por strings.
# Puedes acceder de los elementos utilizando la estructura de arriba.
# En el for exterior, i apunta a cada fila (primero a los números, luego a los strings).
# Por otro lado, en el for interior, j apunta a cada columna en de una determinada fila.
# Es decir, i primero vale, [1, 2, 3], y en ese ciclo, j valdrá 1, 2 y luego 3.
# Luego, i valdrá ['Avión', 'Bombilla', 'Corazón'], y en ese ciclo j valdrá 'Avión', 'Bombilla' y luego 'Corazón'.
# Si utilizas len sobre la lista principal (mat, en este caso), lo que obtendrás será la cantidad de filas (cantidad de listas).
# Para obtener el número de columnas en determinada fila, se utiliza len(lista[número_de_fila]).