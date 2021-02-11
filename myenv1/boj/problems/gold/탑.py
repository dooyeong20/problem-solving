from sys import stdin

n = int(input())
tops = list(map(int, stdin.readline().split()))

s = []      # tops의 높이와 위치를 저장할 스택
ans = [0 for _ in range(n)]    # tops를 역순으로 탐색하며 높은 수가 나왔을 때 pop하여 위치를 저장

# 역순으로 tops를 탐색하며 자기보다 높은 탑(수신이 막히는 탑)을 만나면
# 막은 탑의 정보를 ans 스택에 넣는다.
# 만약 자신보다 낮은 탑이라면 계속해서 진행한다.
for i in range(1, n + 1):
    t = tops[-i]
    j = n - i + 1
    
    # 스택이 비어있다면 곧바로 스택에 추가해준다.
    if not s:
        s.append((t, j))
        continue
    
    # 스택의 top 부분에 있는 높이와 현재 탑의 높이를 비교하여
    # 자신보다 낮은 탑이 있다면 pop을 해버린 후 자신의 위치 정보를
    # ans 에 저장한다.
    while s and s[-1][0] < t:
        ans[s.pop()[1] - 1] = j
        
    
    s.append((t, j))

# 남아 있는 탑의 수만큼 도달하지 못하는 탑이 있는 것이기 때문에
# 0으로 채운다.
while s:
    k = s.pop()[1] - 1
    ans[k] = 0


print(' '.join(map(str, ans)))