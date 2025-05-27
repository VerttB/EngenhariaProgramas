import numpy as np
import time
from functools import lru_cache

# Funções auxiliares
def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def matrix_to_tuple(M):
    return tuple(tuple(row) for row in M)

def tuple_to_matrix(T):
    return [list(row) for row in T]

# Memorização explícita com dicionário
memo = {}

def strassen_dp(A, B):
    key = (matrix_to_tuple(A), matrix_to_tuple(B))
    if key in memo:
        return memo[key]

    n = len(A)
    if n == 1:
        result = [[A[0][0] * B[0][0]]]
        memo[key] = result
        return result

    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen_dp(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen_dp(add_matrix(A21, A22), B11)
    M3 = strassen_dp(A11, sub_matrix(B12, B22))
    M4 = strassen_dp(A22, sub_matrix(B21, B11))
    M5 = strassen_dp(add_matrix(A11, A12), B22)
    M6 = strassen_dp(sub_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen_dp(sub_matrix(A12, A22), add_matrix(B21, B22))

    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    memo[key] = C
    return C

# Exemplo de uso
if __name__ == "__main__":
    size = 64  # Você pode testar com 2, 4, 8, ...
    A = np.random.randint(0, 10, (size, size)).tolist()
    B = np.random.randint(0, 10, (size, size)).tolist()

    start = time.time()
    C = strassen_dp(A, B)
    end = time.time()

    print(f"Resultado:\n{np.array(C)}")
    print(f"Tempo com PD: {end - start:.6f} segundos")
