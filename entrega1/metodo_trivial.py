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