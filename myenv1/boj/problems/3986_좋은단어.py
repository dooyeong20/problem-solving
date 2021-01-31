from sys import stdin

n = int(input())
words = [stdin.readline().strip() for _ in range(n)]
answer = 0

for word in words:
    s = []

    for w in word:
        if not s:
            s.append(w)
            continue

        if s[-1] == w:
            s.pop()
        else:
            s.append(w)
        
    if not s:
        answer += 1
    

print(answer)


