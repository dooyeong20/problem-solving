from sys import stdin

n = int(input())
drinks = list(map(int, stdin.readline().split()))

drinks.sort()

ans = drinks.pop()

for d in drinks:
    ans += d / 2

print(ans)