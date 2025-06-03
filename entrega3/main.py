import time
import random
import matplotlib.pyplot as plt

def water_connection_greedy(n, pipes):
    start = [0] * (n + 1)
    end = [0] * (n + 1)
    diameter = [0] * (n + 1)

    for u, v, d in pipes:
        start[u] = v
        end[v] = u
        diameter[u] = d

    result = []


    for i in range(1, n + 1):
        if end[i] == 0 and start[i] != 0:  # Fonte
            current = i
            min_dia = float('inf')
            while start[current] != 0:
                min_dia = min(min_dia, diameter[current])
                current = start[current]
            result.append((i, current, min_dia))

    return result

def water_connection_dfs(n, pipes):
    graph = {}
    dia = {}

    for u, v, d in pipes:
        graph[u] = v
        dia[u] = d

    result = []

    for u in range(1, n + 1):
        if u not in graph.values() and u in graph: 
            current = u
            min_d = dia[current]

            while current in graph:
                min_d = min(min_d, dia[current])
                current = graph[current]

            result.append((u, current, min_d))

    return result


def teste():
    sizes = [100, 500, 1000, 2000, 5000,10000,50000,100000]
    greedy_times = []
    dfs_times = []

    for size in sizes:
        n = size
        pipes = []
        for i in range(1, n):
            pipes.append((i, i + 1, random.randint(1, 100)))
        print(pipes)
        # Tempo Greedy
        start = time.time()
        water_connection_greedy(n, pipes)
        greedy_times.append(time.time() - start)


        #tempo do dfs
        start = time.time()
        water_connection_dfs(n, pipes)
        dfs_times.append(time.time() - start)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, greedy_times, label='Greedy', marker='o')
    plt.plot(sizes, dfs_times, label='DFS Iterativo', marker='x')
    plt.xlabel('Número de casas (n)')
    plt.ylabel('Tempo de execução (s)')
    plt.title('Comparação entre Greedy e DFS Iterativo\n(Water Connection Problem)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    teste()
