# 시작 16 : 40분
from sys import stdin
from collections import deque

def get_ice_list(arr):
    ice_list = []
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                ice_list.append((i, j)) 
    
    return ice_list

def melt(arr, ice_list):
    for i in range(len(ice_list)):
        x, y = ice_list[i]
        sea_cnt = 0

        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                sea_cnt += 1
        

        melted = arr[x][y] - sea_cnt
        ice_list[i] = [x, y, melted]
    

    for ice in ice_list:
        arr[ice[0]][ice[1]] = max(0, ice[2])
    
    return ice_list

def bfs(ice_list, visited, i, j):
    q = deque([(i, j)])
    visited.add((i, j))

    while q:
        x, y = q.pop()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] > 0 and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))
    

def check(ice_list):
    count = 0
    visited = set()

    for ice in ice_list:
        x, y, cnt = ice

        if cnt <= 0 or (x, y) in visited: continue

        bfs(ice_list, visited, x, y)
        count += 1
    
    return count


n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 0
ice_count = 0

while 1:
    ice_list = get_ice_list(arr)
    if not ice_list:
        ans = 0
        break

    ice_list = melt(arr, ice_list)
    ans += 1

    ice_count = check(ice_list)
    if ice_count > 1:
        break

print(ans)

# 제출 17 : 43