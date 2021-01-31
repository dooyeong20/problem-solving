from sys import stdin

n = int(input())
log = [list(stdin.readline().split()) for _ in range(n)]
s = set()

for name, status in log:
    if status == 'enter':
        s.add(name)
    else:
        s.remove(name)

print('\n'.join(sorted(list(s), reverse=True)))
