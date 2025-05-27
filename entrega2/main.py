from alg_strassen_otimizado import strassen_matrix_otimizado
from alg_strassen import strassen_matrix
from strassenDinamico import strassen_dp
from strassen_iterativo import strassen_iterative_fixed

from graficos import comparar_tempo
import numpy as np
import time
from tabulate import tabulate

inputsQuadrados = [2, 4, 8, 16, 32, 64,]
otimizado = []
dinamico = []
normal = []
iterativo2 = []


seed = 48
np.random.seed(seed)

table_data = []

for i in range(len(inputsQuadrados)):
    matrixA = np.random.randint(1, 100, (inputsQuadrados[i], inputsQuadrados[i]))
    matrixB = np.random.randint(1, 100, (inputsQuadrados[i], inputsQuadrados[i]))
    print(matrixA)
    #usando strassen otimizado
    start = time.process_time()
    resultado = strassen_matrix_otimizado(matrixA,matrixB)
    end = time.process_time()
    otimizado_time = end-start
    otimizado.append(otimizado_time)
    
    #usando metodo iterativo
    start = time.process_time()
    resultado2 = strassen_dp(matrixA,matrixB)
    end = time.process_time()
    dinamico_time = end-start
    dinamico.append(dinamico_time)
    
    #strassen normal
    start = time.process_time()
    resultado = strassen_matrix(matrixA,matrixB)
    end = time.process_time()
    normal_time = end-start
    normal.append(normal_time)
    
    #pilha
    
    start = time.process_time()
    resultado = strassen_iterative_fixed(matrixA,matrixB)
    end = time.process_time()
    iterativo2_time = end-start
    iterativo2.append(iterativo2_time)
    print(resultado)
 
    
    

    table_data.append([
        inputsQuadrados[i],
        f"{otimizado_time:.6f}",
        f"{dinamico_time:.6f}",
        f"{normal_time:.6f}",
        f"{iterativo2_time:.6f}"
    ])

headers = ["Tamanho (n×n)", "Otimizado (s)", "Dinamico (s)", "Strassen (s)",  "Iterativo (s)"]
print(tabulate(table_data, headers=headers, tablefmt="grid", floatfmt=".6f"))

comparar_tempo(otimizado, dinamico,normal,iterativo2, inputsQuadrados)