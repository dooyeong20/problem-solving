from sys import stdin
from collections import deque

# 치즈 구멍과 바깥 구분하기 bfs
def bfs_air():
    q = deque()
    q.append((0, 0))
    visited = {(0, 0)}

    while q:
        r, c = q.popleft()
        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            # 만약 치즈 바깥 쪽이거나 안쪽 치즈 구멍과 연결되는 경우 안쪽 치즈 구멍까지 모두 '-1' 공기 상태로 전이
            if 0 <= nr < x and 0 <= nc < y and (nr, nc) not in visited and (arr[nr][nc] == '0' or arr[nr][nc] == '-1'):
                arr[nr][nc] = '-1'
                visited.add((nr, nc))
                q.append((nr, nc))

# 치즈의 가장자리를 녹이는 bfs
def bfs(r, c, visited):
    q = deque([(r, c)])
    visited.add((r, c))
    cnt[2] = 1

    while q:
        cr, cc = q.popleft()

        for d in dirs:
            nr, nc = cr + d[0], cc + d[1]

            if 0 <= nr < x and 0 <= nc < y:
                # 만약 치즈 가장자리라면 현재 위치를 녹임
                if arr[nr][nc] == '-1' and (nr, nc) not in visited:
                    arr[cr][cc] = '-1'
                    continue

                # 그 옆의 치즈조각에게도 동일하게 전이해줌
                if arr[nr][nc] == '1' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
                    cnt[2] += 1

x, y = map(int, stdin.readline().split())
arr = [list(stdin.readline().split()) for _ in range(x)]
arr[0][0] = '-1'
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
cnt = [0, 0, 0] # 시간의 변화와 1시간 전의 치즈 상태 저장을 위한 리스트
tmp = 0 # 1시간 전의 치즈상태 보관을 위한 리스트
hole = 1

while 1:

    # 바깥 쪽과 연결된 치즈 구멍이 있다면 공기 전이
    if hole:
        bfs_air()
    
    cnt[1] = 0
    visited = set()
    
    # 치즈의 가장자리를 녹이는 bfs 실행과 동시에 치즈의 개수를 추적
    for i in range(x):
        for j in range(y):
            if (i,j) not in visited and arr[i][j] == '1':
                bfs(i, j, visited)
                cnt[1] += cnt[2]

    # 남아있는 치즈가 없다면(종료조건이라면) 종료
    if not cnt[1]:
        break
    
    # 이전의 치즈 개수를 저장
    tmp = cnt[1]

    # 날짜 하루 증가
    cnt[0] += 1

print(cnt[0])
print(tmp)
