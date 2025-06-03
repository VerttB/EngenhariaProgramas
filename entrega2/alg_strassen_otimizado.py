import numpy as np
from metodo_trivial import multiplicacao_tradicional
def divide_matriz(M):
    n = M.shape[0]
    mid = n // 2
    return M[:mid, :mid], M[:mid, mid:], M[mid:, :mid], M[mid:, mid:]

def strassen_matrix_otimizado(A, B):
    t = A.shape[0]
    
    if t == 1:
        return A * B 
    if t <= 64:
        return multiplicacao_tradicional(A,B)
    
    A11, A12, A21, A22 = divide_matriz(A)
    B11, B12, B21, B22 = divide_matriz(B)
    
    P1 = strassen_matrix_otimizado(A11, B12 - B22)
    P2 = strassen_matrix_otimizado(A11 + A12, B22)
    P3 = strassen_matrix_otimizado(A21 + A22, B11)
    P4 = strassen_matrix_otimizado(A22, B21 - B11)
    P5 = strassen_matrix_otimizado(A11 + A22, B11 + B22)
    P6 = strassen_matrix_otimizado(A12 - A22, B21 + B22)
    P7 = strassen_matrix_otimizado(A11 - A21, B11 + B12)
    
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7
    
    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    C = np.vstack((top, bottom))
    
    return C