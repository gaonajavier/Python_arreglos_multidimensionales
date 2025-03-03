#Crear la funcion buscar valor:
def buscar_valor(matriz, valor_buscado):
    posicion = next(((fila, col) for fila, fila_valores in enumerate(matriz)
                     for col, elemento in enumerate(fila_valores) if elemento == valor_buscado), None)

    if posicion:
        print(f"✅ Se encontró {valor_buscado} en la fila {posicion[0]} y columna {posicion[1]}.")
    else:
        print(f"❌ {valor_buscado} no se encontró en la matriz.")


# Solicitar los valores de la matriz (3x3)
matriz = []
print("🔹 Ingresa los valores de la matriz 3x3:")
for i in range(3):
    fila = list(map(int, input(f"Ingrese los 3 valores de la fila {i + 1} separados por 1 espacio: ").split()))
    if len(fila) != 3:
        print("❌ Debes ingresar exactamente 3 valores.")
        exit()
    matriz.append(fila)

# Solicitar el valor a buscar
valor_buscado = int(input("🔍 Registre el número a buscar en la matriz: "))

# Buscar el valor en la matriz
buscar_valor(matriz, valor_buscado)
