from sys import stdin


N = int(input())
villages = []
tot = 0

for _ in range(N):
    x, a = map(int, stdin.readline().split())
    villages.append((x, a))
    tot += a

villages.sort(key=lambda x: x[0])

if tot % 2:
    tot += 1

tot //= 2
tmp = 0


for v in villages:
    tmp += v[1]

    if tmp >= tot:
        print(v[0])
        break
