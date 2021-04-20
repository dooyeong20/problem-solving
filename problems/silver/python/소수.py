from sys import stdin

M = int(stdin.readline())
N = int(stdin.readline())

prime = [1 for _ in range(10001)]
prime[0], prime[1] = 0, 0

for i in range(2, 10001):
    if not prime[i]:
        continue

    for j in range(i*2, 10001, i):
        prime[j] = 0

ans = [0, float('inf')]

for i in range(M, N+1):
    if prime[i]:
        ans[0] += i
        if i < ans[1]:
            ans[1] = i

if not ans[0]:
    print(-1)
else:
    print(str(ans[0]) + '\n' + str(ans[1]))
