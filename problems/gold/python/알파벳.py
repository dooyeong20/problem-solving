from sys import stdin

R, C = map(int, stdin.readline().split())
board = [list(stdin.readline().strip()) for _ in range(R)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
used = set()
ans = [-2, 0]


def dfs(board, r, c):
    ans[1] += 1

    if ans[0] < ans[1]:
        ans[0] = ans[1]
        if ans[0] == 26:
            print(26)
            exit(0)

    for d in dirs:
        nr, nc = r+d[0], c+d[1]

        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in used:
            used.add(board[nr][nc])
            dfs(board, nr, nc)
            ans[1] -= 1
            used.remove(board[nr][nc])


used.add(board[0][0])
dfs(board, 0, 0)

print(ans[0])
