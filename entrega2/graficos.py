import matplotlib.pyplot as plt

def comparar_tempo(otimizado, dinamico, strassen_normal, iterativo_pilha, tamanhos):
    plt.plot(tamanhos, otimizado, 's-', label="Otimizado")
    plt.plot(tamanhos, dinamico, 'd-', label="Dinâmico")
    plt.plot(tamanhos, strassen_normal, 'g-', label="Normal")
    plt.plot(tamanhos, iterativo_pilha, 'b-', label="Com pilha")


    plt.xlabel("Tamanho da matriz (n x n)")
    plt.ylabel("Tempo (segundos)")
    plt.title("Comparação de tempo do algoritmo Strassen para multiplicação de matrizes: Otimizado x PD x Normal x Com Pilha")
    plt.legend()
    plt.grid(True)
    plt.show()