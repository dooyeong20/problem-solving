from collections import deque

def find_fishes():
    q = deque([(shark['x'], shark['y'])])
    visited[shark['x']][shark['y']] = 1

    while q:
        x, y = q.popleft()

        for d in dirs:
            nx, ny = x + d[0], y + d[1]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] <= shark['size']:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

                if 0 < arr[nx][ny] < shark['size'] :
                    fish_list.append((visited[nx][ny] - 1, nx, ny))

def eat_fish(fish):
    global time

    arr[shark['x']][shark['y']] = 0
    shark['x'], shark['y'] = fish[1], fish[2]
    arr[fish[1]][fish[2]] = 9
    shark['eat'] += 1
    time += fish[0]

    if shark['eat'] == shark['size']:
        shark['eat'] = 0
        shark['size'] += 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
shark = {'size': 2, 'x' : 0, 'y' : 0, 'eat' : 0}
dirs =[(-1,0), (0, 1), (1, 0), (0, -1)]
visited = [[0 for _ in range(n)] for _ in range(n)]
time = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            shark['x'], shark['y'] = i, j
            break

fish_list = [1]
first = True

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    fish_list = []
    find_fishes()
    if not fish_list:
        break

    fish_list.sort(key = lambda fish : (fish[0], fish[1], fish[2]))
    eatable_fish = fish_list[0]
    eat_fish(eatable_fish)

print(time)