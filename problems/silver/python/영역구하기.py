from sys import stdin
from collections import deque


def solution(m, n, k, pointList):
    def paint(point):
        x1, y1, x2, y2 = point
        y1, y2 = m - y1, m - y2

        for i in range(y2, y1):
            for j in range(x1, x2):
                mapp[i][j] = 1

    def bfs(row, col):
        q = deque([(row, col)])
        mapp[row][col] = 1
        cnt = 0

        while q:
            r, c = q.pop()
            cnt += 1

            for d in dirs:
                nr, nc = r + d[0], c + d[1]

                if 0 <= nr < m and 0 <= nc < n and mapp[nr][nc] == 0:
                    mapp[nr][nc] = 1
                    q.append((nr, nc))

        return cnt

    cnt = 0
    ans = []
    mapp = [[0 for _ in range(n)] for _ in range(m)]
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    for point in pointList:
        paint(point)

    for i in range(m):
        for j in range(n):
            if mapp[i][j] == 0:
                ans.append(bfs(i, j))
                cnt += 1
    ans.sort()
    ans = str(cnt) + '\n' + ' '.join(map(str, ans))

    return ans


m, n, k = map(int, stdin.readline().split())
pointList = [list(map(int, stdin.readline().split())) for _ in range(k)]

print(solution(m, n, k, pointList))


'''
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
'''
