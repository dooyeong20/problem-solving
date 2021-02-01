from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
trains = [deque([0 for _ in range(20)]) for _ in range(n)]
ans = 0
passed = set()

for _ in range(m):
    c = tuple(map(int, stdin.readline().split()))

    if c[0] == 1:
        trains[c[1]-1][c[2]-1] = 1
    
    elif c[0] == 2:
        trains[c[1]-1][c[2]-1] = 0
        
    elif c[0] == 3:
        trains[c[1]-1][-1] = 0
        trains[c[1]-1].rotate(1)
           
    elif c[0] == 4:
        trains[c[1]-1][0] = 0
        trains[c[1]-1].rotate(-1)

for i in range(n):
    if tuple(trains[i]) in passed:
        continue

    passed.add(tuple(trains[i]))
    ans += 1

print(ans)