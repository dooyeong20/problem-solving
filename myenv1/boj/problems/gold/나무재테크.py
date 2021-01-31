from sys import stdin

def log(arr):
    print()
    for a in arr:
        print(a)
    print()

def spring(ground, trees):
    for i in range(n):
        for j in range(n):
            if not trees[i][j]:
                continue
            trees[i][j].sort()

            for l in range(len(trees[i][j])):
                if ground[i][j] - trees[i][j][l] >= 0:
                    ground[i][j] -= trees[i][j][l]
                    trees[i][j][l] += 1
                else:
                    trees[i][j][l] *= -1
                        

def summer(ground, trees):
    for i in range(n):
        for j in range(n):
            if not trees[i][j]:
                continue

            for l in range(1, len(trees[i][j]) + 1):
                if trees[i][j][-1] > 0:
                    break

                tmp = -(trees[i][j].pop())
                tmp //= 2
                ground[i][j] += tmp


def fall(ground, trees):
    for i in range(n):
        for j in range(n):
            if not trees[i][j]:
                continue
            
            for l in trees[i][j]:
                if l % 5:
                    continue

                for d in range(8):
                    nr, nc = i + dx[d], j + dy[d]

                    if 0 <= nr < n and  0 <= nc < n:
                        trees[nr][nc].append(1)


def winter(ground, addArr):
    for i in range(n):
        for j in range(n):
            ground[i][j] += addArr[i][j]


n,m,k = map(int, stdin.readline().split())
addArr = [list(map(int, stdin.readline().split())) for _ in range(n)]
ground = [[5 for _ in range(n)] for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
answer = 0

for _ in range(m):
    x, y, z = map(int, stdin.readline().split())
    trees[x-1][y-1].append(z)


for _ in range(k):
    # print('---spring----')
    spring(ground, trees)

    # print('---summer---')
    summer(ground, trees)

    fall(ground, trees)

    winter(ground, addArr)


for row in trees:
    for item in row:
        answer += len(item)

print(answer)