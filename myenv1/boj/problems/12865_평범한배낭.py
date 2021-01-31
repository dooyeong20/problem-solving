from sys import stdin

n, k = map(int, stdin.readline().split())
items = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j < items[i-1][0]:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i-1][0]] + items[i-1][1])

print(dp[n][k])