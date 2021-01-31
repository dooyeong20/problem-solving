# 14:30
from sys import stdin

def get_path(dirc, gen):
    path_list = [dirc]
    
    for i in range(gen):
        reverse_idx = len(path_list)
        for j in range(1, reverse_idx + 1):
            path_list.append((path_list[-(2*j - 1)] + 1) % 4)

    return path_list

def add_path(dragon_set, path_list, x, y):
    dragon_set.add((x, y))

    for path in path_list:
        x, y = x + dx[path], y + dy[path]
        dragon_set.add((x, y))

def check_square(r, c):
    for i in range(r, r + 2):
        for j in range(c, c + 2):
            if (i, j) not in dragon_set:
                return False

    return True

def solve():
    cnt = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if check_square(i, j):
                cnt += 1
    return cnt

SIZE = 100
n = int(input())
dragons = [list(map(int, stdin.readline().split())) for _ in range(n)]
dragon_set = set()
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
answer = 0

for dragon in dragons:
    y, x, d, g = dragon

    path_list = get_path(d, g)
    add_path(dragon_set, path_list, x, y)

answer = solve()
print(answer)

# 15:25

# 0:55