import pandas as pd
import matplotlib.pyplot as plt

def comparar_tempo(otimizado, dinamico,  tamanhos):
    plt.plot(tamanhos, otimizado, 's-', label="Otimizado")
    plt.plot(tamanhos, dinamico, 'd-', label="Dinamico")

    plt.xlabel("Tamanho da matriz (n x n)")
    plt.ylabel("Tempo (segundos)")
    plt.title("Comparação de tempo: Strassen vs Tradicional")
    plt.legend()
    plt.grid(True)
    plt.show()