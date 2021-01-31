from sys import stdin

n = int(input())

for _ in range(n):
    w, e = map(int, stdin.readline().split())
    dp = [[0 for _ in range(e+1)] for _ in range(w+1)]

    for i in range(1, e + 1):
        dp[1][i] = i

    for i in range(2, w + 1):
        for j in range(i, e + 1):
            for k in range(j-1, i-2, -1):
                dp[i][j] += dp[i-1][k]
    
    for d in dp:
        print(d)
        

    print(dp[w][e])
