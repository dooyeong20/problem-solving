from sys import stdin

n = int(input())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if not dp[i][j] or not arr[i][j]:
            continue

        if i + arr[i][j] < n:
            dp[i+arr[i][j]][j] += dp[i][j]

        if j + arr[i][j] < n:
            dp[i][j + arr[i][j]] += dp[i][j]
        
        # for d in dp:
        #     print(d)
        # print()
        
print(dp[n-1][n-1])
