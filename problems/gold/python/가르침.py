from sys import stdin
from collections import defaultdict
from itertools import combinations as combi

N, K = map(int, stdin.readline().split())
words = [stdin.readline().strip()[4:-4] for _ in range(N)]
chDic = defaultdict(int)
defaultSet = {'a', 'n', 't', 'i', 'c'}
newWordSet = set()
ans = -1

if K < 5:
    print(0)
else:
    for word in words:
        for ch in word:
            if ch not in defaultSet:
                newWordSet.add(ch)

    k = min(K-5, len(newWordSet))

    for cmb in combi(newWordSet, k):
        cmb = set(cmb)
        tmp = 0

        for word in words:
            for ch in word:
                if ch not in defaultSet and ch not in cmb:
                    break
            else:
                tmp += 1

        if tmp > ans:
            ans = tmp

    print(ans)
