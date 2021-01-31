from sys import stdin

def check(li):
    used = [0] * n
    cnt = 0
    for i in range(n-1):
        cnt += 1
        if li[i] < li[i+1]:
            if li[i+1] - li[i] > 1 or cnt < l:
                return 0

            for j in range(i, i - l, -1):
                if j < 0 or j >= n or used[j]:
                    return 0

                used[j] = 1

        if li[i] > li[i+1]:
            if li[i] - li[i+1] > 1: return 0

            cnt = 0

            for j in range(i+1, i+1+l):
                if j < 0 or j >= n or used[j]:
                    return 0
                used[j] = 1
    
    return 1

n, l = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
ans = 0

for i in range(n):
    if check(arr[i]):
        ans += 1

for i in range(n):
    tmpLi = [0] * n
    for j in range(n):
        tmpLi[j] = arr[j][i]
    
    if check(tmpLi):
        ans += 1


print(ans)