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
        if end[i] == 0 and start[i] != 0:  
            current = i
            min_dia = float('inf')
            while start[current] != 0:
                min_dia = min(min_dia, diameter[current])
                current = start[current]
            result.append((i, current, min_dia))

    return result

def water_connection_dfs(n, pipes):
    from collections import defaultdict

    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    # Construir grafo e calcular grau de entrada
    for u, v, d in pipes:
        graph[u].append((v, d))
        in_degree[v] += 1

    visited = [False] * (n + 1)
    result = []

    def dfs(u, min_dia):
        visited[u] = True
        # Como só existe no máximo uma saída, pega o próximo nó se existir
        if not graph[u]:
            # Nó final (sem saída)
            return u, min_dia
        else:
            v, d = graph[u][0]
            min_dia = min(min_dia, d)
            return dfs(v, min_dia)

    for i in range(1, n + 1):
        if in_degree[i] == 0 and graph[i]:  # fonte
            dest, min_dia = dfs(i, float('inf'))
            result.append((i, dest, min_dia))

    return result


def teste():
    sizes = [100, 500]
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
