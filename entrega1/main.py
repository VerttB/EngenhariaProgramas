from alg_strassen import strassen_matrix
from metodo_trivial import multiplicacao_tradicional
from graficos import comparar_tempo
import numpy as np
import time

inputsQuadrados = [2,4,8,16,32,64,128,256,512,1024]	
strassenTimes = []
trivialTimes = []

seed = 48
np.random.seed(seed)

for i in range (len(inputsQuadrados)):
   matrixA = np.random.randint(1,100 ,(inputsQuadrados[i], inputsQuadrados[i]))
   matrixB = np.random.randint(1,100 ,(inputsQuadrados[i], inputsQuadrados[i]))
   start = time.process_time()
   resultado = strassen_matrix(matrixA,matrixB)
   end = time.process_time()
   strassenTimes.append(end-start)
   start = time.process_time()
   resultado2 = multiplicacao_tradicional(matrixA,matrixB)
   end = time.process_time()
   trivialTimes.append(end-start)
   
   resultado =multiplicacao_tradicional(matrixA,matrixB)
   print(f"Strassen com input {inputsQuadrados[i]} deu tempo {strassenTimes[i]}")
   print(f"Trivial com input {inputsQuadrados[i]} deu tempo {trivialTimes[i]}")

comparar_tempo(strassenTimes,trivialTimes, inputsQuadrados)

    
