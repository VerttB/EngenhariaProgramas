
import numpy as np
import time

def add_matriz(A, B):
    t = len(A)
    return [[A[i][j] + B[i][j] for j in range(t)] for i in range(t)]


def sub_matriz(A, B):
    t = len(A)
    return [[A[i][j] - B[i][j] for j in range(t)] for i in range(t)]


def divide_matriz(M):
    n = len(M)
    mid = n // 2
    M11 = M[:mid, :mid]
    M12 = M[:mid, mid:]
    M21 = M[mid:, :mid]
    M22 = M[mid:, mid:]
    return M11, M12, M21, M22

def strassenMatrix(A, B):
    start = time.process_time()
    t = len(A)
    
    if t < 2:
        return np.dot(A, B)
    
    A11, A12, A21, A22 = divide_matriz(A)
    B11, B12, B21, B22 = divide_matriz(B)
    
    P1 = strassenMatrix(A11, B12 - B22)
    P2 = strassenMatrix(A11 + A12, B22)
    P3 = strassenMatrix(A21 + A22, B11)
    P4 = strassenMatrix(A22, B21 - B11)
    P5 = strassenMatrix(A11 + A22, B11 + B22)
    P6 = strassenMatrix(A12 - A22, B21 + B22)
    P7 = strassenMatrix(A11 - A21, B11 + B12)
    
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7
    
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    end = time.process_time()
    return C, (end-start)
    
A = np.array([[1, 3], [7, 5]])
B = np.array([[6, 8], [4, 2]])
C,time = strassenMatrix(A, B)

print(f"Tempo de duração {time:16f}")
print(C)

