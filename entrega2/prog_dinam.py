import numpy as np

def divide_matriz(M):
    n = M.shape[0]
    mid = n // 2
    return M[:mid, :mid], M[:mid, mid:], M[mid:, :mid], M[mid:, mid:]

# Versão com Programação Dinâmica (memoização)
def matrix_prog_dinam(A, B, memo=None):
    if memo is None:
        memo = {}
    
    t = A.shape[0]
    key = (tuple(A.ravel()), tuple(B.ravel()))  # Chave única para memoização
    
    if key in memo:
        return memo[key]
    
    if t == 1:
        memo[key] = A * B
        return memo[key]
    
    A11, A12, A21, A22 = divide_matriz(A)
    B11, B12, B21, B22 = divide_matriz(B)
    
    # Calcula P1 a P7 com memoização
    P1 = matrix_prog_dinam(A11, B12 - B22, memo)
    P2 = matrix_prog_dinam(A11 + A12, B22, memo)
    P3 = matrix_prog_dinam(A21 + A22, B11, memo)
    P4 = matrix_prog_dinam(A22, B21 - B11, memo)
    P5 = matrix_prog_dinam(A11 + A22, B11 + B22, memo)
    P6 = matrix_prog_dinam(A12 - A22, B21 + B22, memo)
    P7 = matrix_prog_dinam(A11 - A21, B11 + B12, memo)
    
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7
    
    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    C = np.vstack((top, bottom))
    
    memo[key] = C
    return C