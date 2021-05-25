
from sys import stdin
from collections import deque

V = int(stdin.readline())
adjList = [[] for _ in range(V + 1)]
distances = [0 for _ in range(V + 1)]
dot = [0, 0]

for _ in range(V):
    info = list(map(int, stdin.readline().split()))
    v = info[0]
    idx = 1

    while info[idx] != -1:
        adjList[v].append((info[idx], info[idx+1]))
        idx += 2


def bfs(i, j):
    q = deque()
    v = [False] * (V + 1)
    distances[i] = 0
    q.append(i)
    v[i] = True
    maxDist = -1

    while q:
        cur = q.popleft()

        for adj in adjList[cur]:
            if v[adj[0]]:
                continue

            v[adj[0]] = True
            q.append(adj[0])
            distances[adj[0]] = distances[cur] + adj[1]

            if distances[adj[0]] > maxDist:
                maxDist = distances[adj[0]]
                dot[j] = adj[0]


bfs(1, 0)       # 지름을 구성하는 노드 중 하나를 먼저 구하는 bfs
bfs(dot[0], 1)  # 지름을 구성하는 한 노드를 알 때, 나머지 노드를 구해주면서 가중치의 합을 구해주는 bfs

print(distances[dot[1]])
