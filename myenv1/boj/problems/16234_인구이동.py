from sys import stdin
from collections import deque

def check():
    moved = 0
    union_arr = [[0 for _ in range(n)] for _ in range(n)]
    flag = 1

    for i in range(n):
        for j in range(n):
            if union_arr[i][j] == 0:
                is_union = 0
                q = deque([(i, j)])
                union_arr[i][j] = flag

                while q:
                    x, y = q.pop()

                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]

                        if 0 <= nx < n and 0 <= ny < n and not union_arr[nx][ny] and l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                            
                            is_union = 1
                            union_arr[nx][ny] = flag
                            q.append((nx, ny))
                
                if not is_union:
                    union_arr[i][j] = 0
                    flag -= 1
                
                flag += 1

    if flag > 1:
        moved = 1

    return (moved, union_arr)


def bfs(i, j):
    q = deque([(i, j)])
    union_loc = {(i, j)}
    flag = union_arr[i][j]
    union_arr[i][j] = 0
    total = arr[i][j]
    cnt = 1

    while q:
        x, y = q.pop()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if (nx, ny) not in union_loc and 0 <= nx < n and 0 <= ny < n and union_arr[nx][ny] == flag:
                total += arr[nx][ny]
                cnt += 1
                q.append((nx, ny))
                union_arr[nx][ny] = 0
                union_loc.add((nx, ny))

    return (total // cnt, union_loc) 
    

def move(location, avg):
    for loc in location:
        x, y = loc
        arr[x][y] = avg

n, l, r = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
union_arr = []
ans = 0


while 1:
    moved, union_arr = check()

    if not moved:
        break
    
    for i in range(n):
        for j in range(n):
            if union_arr[i][j] > 0:
                avg, loc = bfs(i, j)
                move(loc, avg)

    ans += 1

print(ans)