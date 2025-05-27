import pandas as pd
import matplotlib.pyplot as plt

def comparar_tempo(otimizado, dinamico, strassen,pilha, tamanhos):
    plt.plot(tamanhos, otimizado, 's-', label="Otimizado")
    plt.plot(tamanhos, dinamico, 'd-', label="Dinamico")
    plt.plot(tamanhos, strassen, 'g-', label="Strassen")
    plt.plot(tamanhos, pilha, 'b-', label="pilha")


    plt.xlabel("Tamanho da matriz (n x n)")
    plt.ylabel("Tempo (segundos)")
    plt.title("Comparação de tempo: Strassen vs Tradicional")
    plt.legend()
    plt.grid(True)
    plt.show()