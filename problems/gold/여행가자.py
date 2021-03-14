from sys import stdin


def find(x):
    if p[x] == x:
        return x

    p[x] = find(p[x])
    return p[x]

def union(x, y):
    if p[x] == p[y]:
        return
    
    p[find(y)] = find(x)

n = int(stdin.readline())
m = int(stdin.readline())

p = dict()

for i in range(n):
    info = list(map(int, stdin.readline().split()))

    if i not in p:
        p[i] = i
        
    for j in range(n):
        if info[j] == 0:
            continue

        if j not in p:
            p[j] = j
        
        union(i, j)
    
trip = list(map(int, stdin.readline().split()))
ans = 'YES'
tmp = find(trip[0] - 1)

for city in trip:
    if tmp != find(city - 1):
        ans = 'NO'

print(ans)
