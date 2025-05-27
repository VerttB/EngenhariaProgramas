from alg_strassen import strassen_matrix
from prog_dinam import matrix_prog_dinam
from graficos import comparar_tempo
import numpy as np
import time
from tabulate import tabulate

inputs_quadrados = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
strassen_times = []
prog_dinam_times = []
recursivaMult = []
seed = 48
np.random.seed(seed)

table_data = []

for i in range(len(inputs_quadrados)):
    matrixA = np.random.randint(1, 100, (inputs_quadrados[i], inputs_quadrados[i]))
    matrixB = np.random.randint(1, 100, (inputs_quadrados[i], inputs_quadrados[i]))
    
    #usando strassen simples
    start = time.process_time()
    resultado = strassen_matrix(matrixA,matrixB)
    end = time.process_time()
    strassen_time = end-start
    strassen_times.append(strassen_time)
    
    #usando strassen com programação dinâmica
    start = time.process_time()
    resultado2 = matrix_prog_dinam(matrixA,matrixB)
    end = time.process_time()
    prog_dinam_time = end-start
    prog_dinam_times.append(prog_dinam_time)
    

    table_data.append([
        inputs_quadrados[i],
        f"{strassen_time:.6f}",
        f"{prog_dinam_time:.6f}",
    ])

headers = ["Tamanho (n×n)", "Strassen simples (s)", "Strassen PD (s)"]
print(tabulate(table_data, headers=headers, tablefmt="grid", floatfmt=".6f"))

comparar_tempo(strassen_times, prog_dinam_times, inputs_quadrados)