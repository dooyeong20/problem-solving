from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

dp = [0] * n
ans = 0

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j]:
            dp[i] = dp[j]
    
    dp[i] += arr[i]
    if ans < dp[i]:
        ans = dp[i]
    # print(dp)

print(ans)