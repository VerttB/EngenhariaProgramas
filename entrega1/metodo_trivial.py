import numpy as np
import time

def multiplicacao_tradicional(A, B):
    n = len(A)
    C = np.zeros((n, n), dtype=int)  # Matriz de resultado
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

# # Exemplo de uso:
# A = np.array([[1, 3], [7, 5]])
# B = np.array([[6, 8], [4, 2]])

# C, tempo = multiplicacao_tradicional(A, B)
# print(f"Tempo (Tradicional): {tempo:.6f} segundos")
# print("Resultado:\n", C)