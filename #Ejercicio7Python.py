#Ejercicio7Python
valores = [5, 1, 9, 2, 7, 4]
encontrado = False
indice = 0
longitud = len(valores)
while indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
        break
    else:
        indice += 1
if encontrado:
    print(f'El elemento 2 ha sido encontrado en el índice {indice}')
else:
    print('El elemento 2 no se encuentra en la lista de valores')