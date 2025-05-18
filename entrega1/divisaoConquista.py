import numpy as np

def divide_matriz(M):
    n = len(M)
    mid = n // 2
    M11 = M[:mid, :mid]
    M12 = M[:mid, mid:]
    M21 = M[mid:, :mid]
    M22 = M[mid:, mid:]
    return M11, M12, M21, M22

def multiplicacao_recursiva(A, B):
    n = A.shape[0]
    if n == 1:
        return A * B
    A11, A12, A21, A22 = divide_matriz(A)
    B11, B12, B21, B22 = divide_matriz(B)
    C11 = multiplicacao_recursiva(A11, B11) + multiplicacao_recursiva(A12, B21)
    C12 = multiplicacao_recursiva(A11, B12) + multiplicacao_recursiva(A12, B22)
    C21 = multiplicacao_recursiva(A21, B11) + multiplicacao_recursiva(A22, B21)
    C22 = multiplicacao_recursiva(A21, B12) + multiplicacao_recursiva(A22, B22)
    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    C = np.vstack((top, bottom))
    return C