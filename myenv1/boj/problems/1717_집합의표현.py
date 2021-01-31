from sys import stdin


def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])

    return parent[x]


def union(x, y):
    if find(x) == find(y):
        return

    parent[find(y)] = find(x)


n, m = map(int, stdin.readline().split())
parent = dict()

for _ in range(m):
    cmd, a, b = map(int, stdin.readline().split())

    if a not in parent:
        parent[a] = a
    
    if b not in parent:
        parent[b] = b

    
    if cmd:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
        continue

    union(a, b)
