from sys import stdin


def solution(N, M, trees):
    def check(m):
        res = 0

        for t in trees:
            res += t - m if t > m else 0

        return res

    l, r = 0, 2000000000

    while l <= r:
        m = (l+r)//2

        if check(m) > M:
            l = m + 1
        else:
            r = m - 1

    if check(r+1) < M:
        r -= 1

    return r + 1


N, M = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

print(solution(N, M, trees))
