from sys import stdin

def solve(n):
    if n == 1:
        return 0

    if n < 4:
        return 1

    dp = [0 for _ in range(n + 1)]

    dp[2] = 1
    dp[3] = 1

    for i in range(4, n+1):
        dp[i] = dp[i-1]
        
        if not i % 2:
            dp[i] = min(dp[i], dp[i//2])
        
        if not i % 3:
            dp[i] = min(dp[i], dp[i//3])
        
        dp[i] += 1
    
    return dp[n]


n = int(input())
print(solve(n))