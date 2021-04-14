from sys import stdin

h, w = map(int, stdin.readline().split())
blocks = list(map(int, stdin.readline().split()))
arr = [[0 for _ in range(w)] for _ in range(h)]
ans = 0

# 2차원 세계에 블록 쌓기
for i in range(w):
    for j in range(blocks[i]):
        arr[-j-1][i] = 1

# 2차원 세계 배열을 순회하며 stack을 이용해
# 블록 사이에 있는 공백의 수량(빗물)을 세준다
for row in arr:
    s = []
    for a in row:
        # 1일 경우(블록일 경우) 쌓인 빗물이 있다면 세주고
        # stack을 1로 초기화한다.
        if a == 1:
            while s and s[-1] != 1:
                ans += 1
                s.pop()
            s = [1]

        # 0일 경우(빗물이 들어갈 수 있는 조건 중 하나일 경우)
        # stack의 empty여부(빗물이 세어나가지 않도록 블록이 있는 경우)에
        # 빗물을 받아준다(stack에 넣어준다).
        if a == 0 and s:
            s.append(0)

# 쌓인 빗물을 출력해준다
print(ans)