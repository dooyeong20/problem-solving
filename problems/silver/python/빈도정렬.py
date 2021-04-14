from sys import stdin

n, c = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

dic = dict()

for n in nums:
    if n not in dic:
        dic[n] = 1
        continue

    dic[n] += 1

dic = list(dic.items())
dic.sort(key=lambda x : -x[1])

answer = ''
for d in dic:
    answer += (str(d[0]) + ' ') * d[1]

print(answer)