import pandas as pd
import matplotlib.pyplot as plt

def comparar_tempo(tempos_strassen, tempos_trivial, tamanhos):
    
    plt.plot(tamanhos, tempos_strassen, 'o-', label="Strassen")
    plt.plot(tamanhos, tempos_trivial, 's-', label="Tradicional")
    plt.xlabel("Tamanho da matriz (n x n)")
    plt.ylabel("Tempo (segundos)")
    plt.title("Comparação de tempo: Strassen vs Tradicional")
    plt.legend()
    plt.grid(True)
    plt.show()