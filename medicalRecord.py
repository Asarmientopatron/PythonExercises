data = [
  [1, 'M', 66, 52],
  [1, 'F', 208, 129],
  [1, 'F', 86, 46],
  [1, 'F', 137, 84],
  [1, 'F', 204, 125],
  [1, 'M', 65, 42],
  [1, 'M', 135, 72],
  [1, 'F', 135, 86],
  [2, 'F', 201, 132],
  [2, 'F', 192, 117],
  [2, 'F', 191, 127],
  [2, 'F', 54, 48],
  [2, 'F', 56, 45],
  [2, 'M', 206, 141],
  [2, 'M', 200, 121],
  [2, 'M', 202, 144],
  [3, 'F', 88, 51],
  [3, 'M', 159, 75],
  [3, 'M', 115, 72],
  [3, 'M', 104, 77],
  [3, 'F', 67, 49],
  [3, 'M', 187, 136],
  [3, 'M', 205, 144],
  [3, 'F', 80, 60],
  [3, 'M', 208, 126],
  [3, 'M', 66, 62],
  [3, 'M', 100, 97],
  [3, 'M', 191, 148],
]

campusName = ['Alcalá', 'El Centro', 'La Magnolia']
treatedWomen = [0, 0, 0]
treatedMen = [0, 0, 0]
medicatedWomen = [0, 0, 0]
medicatedMen = [0, 0, 0]
lowPressGiven = [0, 0, 0]
highPressGiven = [0, 0, 0]
averageSisPress = [0, 0, 0]
averageDiasPress = [0, 0, 0]
text = """------------------------------------------------
  Sede: {}
  Pacientes Femeninos Atendidos: {}
  Pacientes Masculino Atendidos: {}
  Pacientes Femeninos Medicados: {}
  Pacientes Masculinos Medicados: {}
  Medicamentos para Hipotensión Entregados: {}
  Medicamentos para Hipertensión Entregados: {}
  Presión Sistólica Media: {}
  Presión Diastólica Media: {}
------------------------------------------------"""

# for i in data:
#   if i[0] == 1:
#     averageSisPress[0] += i[2]
#     averageDiasPress[0] += i[3]
#     if i[1] == 'F':
#       treatedWomen[0] += 1
#       if i[2] < 91 and i[3] < 63:
#         medicatedWomen[0] += 1
#         lowPressGiven[0] += 1
#       if i[2] > 188 and i[3] > 119:
#         medicatedWomen[0] += 1
#         highPressGiven[0] += 1
#     else:
#       treatedMen[0] += 1
#       if i[2] < 91 and i[3] < 63:
#         medicatedMen[0] += 1
#         lowPressGiven[0] += 1
#       if i[2] > 188 and i[3] > 119:
#         medicatedMen[0] += 1
#         highPressGiven[0] += 1
#   elif i[0] == 2:
#     averageSisPress[1] += i[2]
#     averageDiasPress[1] += i[3]
#     if i[1] == 'F':
#       treatedWomen[1] += 1
#       if i[2] < 91 and i[3] < 63:
#         medicatedWomen[1] += 1
#         lowPressGiven[1] += 1
#       if i[2] > 188 and i[3] > 119:
#         medicatedWomen[1] += 1
#         highPressGiven[1] += 1
#     else:
#       treatedMen[1] += 1
#       if i[2] < 91 and i[3] < 63:
#         medicatedMen[1] += 1
#         lowPressGiven[1] += 1
#       if i[2] > 188 and i[3] > 119:
#         medicatedMen[1] += 1
#         highPressGiven[1] += 1
#   else:
#     averageSisPress[2] += i[2]
#     averageDiasPress[2] += i[3]
#     if i[1] == 'F':
#       treatedWomen[2] += 1
#       if i[2] < 91 and i[3] < 63:
#         medicatedWomen[2] += 1
#         lowPressGiven[2] += 1
#       if i[2] > 188 and i[3] > 119:
#         medicatedWomen[2] += 1
#         highPressGiven[2] += 1
#     else:
#       treatedMen[2] += 1
#       if i[2] < 91 and i[3] < 63:
#         medicatedMen[2] += 1
#         lowPressGiven[2] += 1
#       if i[2] > 188 and i[3] > 119:
#         medicatedMen[2] += 1
#         highPressGiven[2] += 1

for i in data:
  averageSisPress[i[0]-1] += i[2]
  averageDiasPress[i[0]-1] += i[3]
  if i[1] == 'F':
    treatedWomen[i[0]-1] += 1
    if i[2] < 91 and i[3] < 63:
      medicatedWomen[i[0]-1] += 1
      lowPressGiven[i[0]-1] += 1
    if i[2] > 188 and i[3] > 119:
      medicatedWomen[i[0]-1] += 1
      highPressGiven[i[0]-1] += 1
  else:
    treatedMen[i[0]-1] += 1
    if i[2] < 91 and i[3] < 63:
      medicatedMen[i[0]-1] += 1
      lowPressGiven[i[0]-1] += 1
    if i[2] > 188 and i[3] > 119:
      medicatedMen[i[0]-1] += 1
      highPressGiven[i[0]-1] += 1

for i in range(0, 3):
  print(text.format(
    campusName[i],
    treatedWomen[i],
    treatedMen[i],
    medicatedWomen[i],
    medicatedMen[i],
    lowPressGiven[i],
    highPressGiven[i],
    averageSisPress[i]/(treatedMen[i]+treatedWomen[i]),
    averageDiasPress[i]/(treatedMen[i]+treatedWomen[i]),
  ))