from sys import stdin
import heapq


def solution(n, m, infos):
    ans = ''
    in_branch = [0 for _ in range(n+1)]
    h = []
    dic = {k: [] for k in range(1, n+1)}

    for a, b in infos:
        in_branch[b] += 1
        dic[a].append(b)

    for i in range(1, n+1):
        if in_branch[i] > 0:
            continue

        heapq.heappush(h, i)

    while h:
        tmp = heapq.heappop(h)
        for d in dic[tmp]:
            in_branch[d] -= 1
            if in_branch[d] < 1:
                heapq.heappush(h, d)

        ans += str(tmp) + ' '

    return ans


n, m = map(int, stdin.readline().split())
infos = [list(map(int, stdin.readline().split())) for _ in range(m)]
print(solution(n, m, infos))

'''
> 입력

8 4
5 3
3 2
4 6
2 8

> 정답 : 1 4 5 3 2 6 7 8
'''
