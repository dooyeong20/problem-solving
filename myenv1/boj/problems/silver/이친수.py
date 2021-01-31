from sys import stdin

n = int(input())

dp = [[0, 0] for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = 1

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

ans = sum(dp[n])
print(ans)

'''

1
10
100 101
1000 1001 1010


'''