import matplotlib.pyplot as plt

def comparar_tempo(tempos_strassen, programacao_dinamica, tamanhos):
    plt.plot(tamanhos, tempos_strassen, 'o-', label="Strassen Simples", color='blue')
    plt.plot(tamanhos, programacao_dinamica, 's-', label="Strassen PD", color='red')

    plt.xlabel("Tamanho da matriz (n x n)")
    plt.ylabel("Tempo (segundos)")
    plt.title("Comparação de tempo: Strassen Simples vs Strassen PD")
    plt.legend()
    plt.grid(True)
    plt.show()