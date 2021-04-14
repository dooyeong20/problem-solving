from sys import stdin

# def print_arr(arr):
#     for a in arr:
#         print(a)
#     print()

def get_cleaner_top():
    for i in range(r):
        if arr[i][0] == -1:
            return i

def spread():
    total = 0
    tmp_arr = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:

                amount = arr[i][j]
                split_amount = amount // 5
                split_cnt = 0

                for d in range(4):
                    x, y = i + dx[d], j + dy[d]

                    if 0 <= x < r and 0 <= y < c and arr[x][y] > -1:
                        split_cnt += 1
                        tmp_arr[x][y] += split_amount

                tmp_arr[i][j] -= split_amount * split_cnt
                
    for i in range(r):
        for j in range(c):
            if arr[i][j] == -1: continue
            arr[i][j] += tmp_arr[i][j]
            total += arr[i][j]

    return total
    

def clean(X, y, d, reverse):
    global total_cnt

    if reverse:
        x = X + 1
    else:
        x = X - 1

    total_cnt -= arr[x][y]

    while 1:

        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= r or ny < 0 or ny >= c or (not reverse and nx > X) or (reverse and nx < X):
            if reverse:
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
            continue

        if arr[nx][ny] == -1:
            arr[x][y] = 0
            return
        
        arr[x][y] = arr[nx][ny]
        x, y = nx, ny

    return removed


r, c, t = map(int, stdin.readline().split())

arr = [list(map(int, stdin.readline().split())) for _ in range(r)]
cleaner_top = get_cleaner_top()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
total_cnt = 0

for _ in range(t):
    total_cnt = spread()
    # print_arr(arr)
    clean(cleaner_top, 0, 0, 0)
    clean(cleaner_top + 1, 0, 2, 1)
    # print_arr(arr)

print(total_cnt)