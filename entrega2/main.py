from alg_strassen_otimizado import strassen_matrix
from strassenDinamico import strassen_dp
from graficos import comparar_tempo
import numpy as np
import time
from tabulate import tabulate

inputsQuadrados = [2, 4, 8, 16, 32, 64]
otimizado = []
iterativo = []
seed = 48
np.random.seed(seed)

table_data = []

for i in range(len(inputsQuadrados)):
    matrixA = np.random.randint(1, 100, (inputsQuadrados[i], inputsQuadrados[i]))
    matrixB = np.random.randint(1, 100, (inputsQuadrados[i], inputsQuadrados[i]))
    
    #usando strassen
    start = time.process_time()
    resultado = strassen_matrix(matrixA,matrixB)
    end = time.process_time()
    otimizado_time = end-start
    otimizado.append(otimizado_time)
    
    #usando metodo trivial
    start = time.process_time()
    resultado2 = strassen_dp(matrixA,matrixB)
    end = time.process_time()
    iterativo_time = end-start
    iterativo.append(iterativo_time)
    
    #usando divisão e conquista básica com recursão
    
    

    table_data.append([
        inputsQuadrados[i],
        f"{otimizado_time:.6f}",
        f"{iterativo_time:.6f}",
    ])

headers = ["Tamanho (n×n)", "Tradicional (s)", "Divisão/Conquista (s)", "Strassen (s)"]
print(tabulate(table_data, headers=headers, tablefmt="grid", floatfmt=".6f"))

comparar_tempo(otimizado, iterativo, inputsQuadrados)