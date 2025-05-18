from alg_strassen import strassen_matrix
from metodo_trivial import multiplicacao_tradicional
from divisaoConquista import multiplicacao_recursiva
from graficos import comparar_tempo
import numpy as np
import time
from tabulate import tabulate

inputsQuadrados = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
strassenTimes = []
trivialTimes = []
recursivaMult = []
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
    strassen_time = end-start
    strassenTimes.append(strassen_time)
    
    #usando metodo trivial
    start = time.process_time()
    resultado2 = multiplicacao_tradicional(matrixA,matrixB)
    end = time.process_time()
    trivial_time = end-start
    trivialTimes.append(trivial_time)
    
    #usando divisão e conquista básica com recursão
    start = time.process_time()
    resultado = multiplicacao_recursiva(matrixA,matrixB)
    end = time.process_time()
    recursiva_time = end-start
    recursivaMult.append(recursiva_time)
    

    table_data.append([
        inputsQuadrados[i],
        f"{trivial_time:.6f}",
        f"{recursiva_time:.6f}",
        f"{strassen_time:.6f}"
    ])

headers = ["Tamanho (n×n)", "Tradicional (s)", "Divisão/Conquista (s)", "Strassen (s)"]
print(tabulate(table_data, headers=headers, tablefmt="grid", floatfmt=".6f"))

comparar_tempo(trivialTimes, recursivaMult, strassenTimes, inputsQuadrados)