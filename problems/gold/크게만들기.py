from sys import stdin

n, k = map(int, stdin.readline().split())
numS = stdin.readline().strip()
cnt = 0
s = []

for num in numS:
    num = int(num)

    if not s:
        s.append(num)
        continue

    while s and cnt < k and num > s[-1]:
        s.pop()
        cnt += 1
    
    s.append(num)

while cnt < k:
    s.pop()
    cnt += 1

print(''.join(map(str, s)))