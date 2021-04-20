from sys import stdin

N, M = map(int, stdin.readline().split())
arr = [0 for _ in range(1001)]

ans = 0
num = 0
cnt = 0

for i in range(1001):
    if i > M:
        break

    arr[i] = num

    if i >= cnt:
        num += 1
        cnt += num

    if N <= i <= M:
        ans += arr[i]

print(ans)
