from alg_strassen import strassen_matrix
from metodo_trivial import multiplicacao_tradicional
from divisaoConquista import multiplicacao_recursiva
from graficos import comparar_tempo
import numpy as np
import time

inputsQuadrados = [2,4,8,16,32,64,128,256,512,1024]	
strassenTimes = []
trivialTimes = []
recursivaMult = []
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
   
   
   start = time.process_time()
   resultado = multiplicacao_recursiva(matrixA,matrixB)
   end = time.process_time()
   recursivaMult.append(end-start)
   print(f"Strassen com input {inputsQuadrados[i]} deu tempo {strassenTimes[i]}")
   print(f"Trivial com input {inputsQuadrados[i]} deu tempo {trivialTimes[i]}")
   print(f"Reecursiva Divisao Conquista {inputsQuadrados[i]} deu tempo { recursivaMult[i]}")
comparar_tempo(strassenTimes,trivialTimes,recursivaMult, inputsQuadrados)

    
