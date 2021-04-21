from sys import stdin


def check_right(board1, board2, a, b):
    if board1[a][b:b+2] != board2[a][b:b+2]:
        return False

    return True


def check_bottom(board1, board2, a, b):
    for i in range(a, a+2):
        if board1[i][b] != board2[i][b]:
            return False

    return True


def flip(board, a, b):
    for i in range(a, a+3):
        for j in range(b, b+3):
            board[i][j] = '1' if board[i][j] == '0' else '0'


N, M = map(int, stdin.readline().split())
A = [list(stdin.readline().strip()) for _ in range(N)]
B = [list(stdin.readline().strip()) for _ in range(N)]
ans = 0

if N < 3 or M < 3:
    if A != B:
        print(-1)
    else:
        print(0)
    exit(0)

for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip(A, i, j)
            ans += 1

        if j == M-3 and not check_right(A, B, i, j+1):
            print(-1)
            exit(0)

        if i == N-3 and not check_bottom(A, B, i+1, j):
            print(-1)
            exit(0)

for i in range(N-2, N):
    for j in range(M-2, M):
        if A[i][j] != B[i][j]:
            print(-1)
            exit(0)

print(ans)

'''
3 3
111
111
111
000
000
000
'''
