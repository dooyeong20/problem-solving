from sys import stdin
from itertools import combinations

def log(arr):
    print('------')
    for a in arr:
        print(a)
    print('------')

def go_down():
    for i in range(v):
        cr, cc = 0, i

        while cr < h:
            if ladder[cr][cc] == 0:
                cr += 1
                continue

            if ladder[cr][cc] == 1:
                cr += 1
                cc += 1
                continue

            if ladder[cr][cc] == -1:
                cr += 1
                cc -= 1
        if i != cc:
            return 0

    return 1

def add_and_check():
    for i in range(1, 4):
        for comb in combinations(addable, i):
            for r, c in comb:
                ladder[r][c] = 1
                ladder[r][c+1] = -1
            
            if go_down():
                return i
            
            for r, c in comb:
                ladder[r][c] = 0
                ladder[r][c+1] = 0
    
    return -1

v, n, h = map(int, stdin.readline().split()) 

answer = 0
ladder = [[0 for _ in range(v)] for _ in range(h+1)]
lines = [list(map(int, stdin.readline().split())) for _ in range(n)]
addable = []

for r, c in lines:
    ladder[r-1][c-1] = 1    # go right
    ladder[r-1][c] = -1     # go left

for i in range(h):
    for j in range(v-1):
        if ladder[i][j] or ladder[i][j+1]:
            continue
        
        addable.append((i,j))

if not go_down():
    answer = add_and_check()

print(answer)