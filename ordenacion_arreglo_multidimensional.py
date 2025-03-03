def bubble_sort(lista):
    """Ordena una lista usando el algoritmo Bubble Sort."""
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:  # Intercambio si está en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def ordenar_fila(matriz, fila_index):
    """Ordena una fila específica de la matriz utilizando Bubble Sort."""
    if 0 <= fila_index < len(matriz):  # Verifica que la fila exista
        bubble_sort(matriz[fila_index])  # Aplica Bubble Sort en la fila elegida
    else:
        print("❌ Índice de fila fuera de rango.")

# Solicitar el tamaño de la matriz (n x n)
n = int(input("🔹 Ingrese el tamaño de la matriz (n x n): "))

# Solicitar los valores de la matriz
matriz = []
print(f"🔹 Ingresa los {n**2} valores de la matriz:")
for i in range(n):
    fila = list(map(int, input(f"Ingrese los {n} valores de la fila {i + 1} separados por espacios: ").split()))
    if len(fila) != n:
        print("❌ Debes ingresar exactamente", n, "valores.")
        exit()
    matriz.append(fila)

# Mostrar matriz original
print("\n🔢 Matriz original:")
for fila in matriz:
    print(fila)

# Solicitar la fila a ordenar
fila_index = int(input(f"🔄 Ingrese el número de fila (0 a {n-1}) que desea ordenar: "))

# Ordenar la fila especificada
ordenar_fila(matriz, fila_index)

# Mostrar matriz después de ordenar la fila
print("\n✅ Matriz después de ordenar la fila:")
for fila in matriz:
    print(fila)
