from sys import stdin
from collections import deque

# def log(arr):
#     for a in arr:
#         print(a)

def bfs(r, c, arr):
    q = deque()
    q.append((r,c))
    visit = set()
    visit.add((r,c))

    while q:
        cr, cc = q.popleft()

        for i in range(8):
            nr, nc = cr + dx[i], cc + dy[i]

            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                if [nr, nc] == goal:
                    return arr[cr][cc] + 1

                visit.add((nr, nc))
                arr[nr][nc] = arr[cr][cc] + 1
                q.append((nr, nc))
            

t = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

for _ in range(t):
    n = int(input())
    r, c = map(int, stdin.readline().split())
    goal = list(map(int, stdin.readline().split()))
    if [r, c] == goal:
        print(0)
        contin
    arr = [[0 for _ in range(n)] for _ in range(n)]
    
    print(bfs(r, c, arr))
