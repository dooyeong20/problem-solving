from sys import stdin

t = int(input())
nums = []
idx = 1
tmp = 0

# nums 리스트에 2, 4, 6, 8, 10 ... 을 누적해서 더해가는 값을
# 저장해줌
while 1:
    tmp += idx*2
    if tmp > pow(2, 31):
        break
    nums.append(tmp)
    idx += 1

# 각 testcase별로 x,y 에 대해서 양쪽 끝에서부터
# 1, 2, 3 씩 차례대로 이동하며 가운데에서 남는 부분을
# 기준으로 분기처리해서 값을 구해줌
for _ in range(t):
    x, y = map(int, stdin.readline().split())
    k = y - x
    
    # 만약 거리차이가 1이라면 1을 리턴
    if k == 1:
        print(1)
        continue
    
    tmpI = 0

    # 거리차이가 2 이상인 경우 양쪽 끝에서부터
    # 1,2,3씩 구해나간 거리를 뺀 나머지 거리와 그 때의
    # 최종 숫자를 구함
    for i, n in enumerate(nums):
        if k >= n:
            tmp = n
            tmpI += 1
            continue
        break
    
    
    k -= tmp
    
    # 만약 남은 자투리 거리가 0이라면, 양쪽이 대칭을 이루고 있다는
    # 뜻이므로 현재 숫자 값을 2배해줌
    if k == 0:
        tmpI *= 2
    
    # 만약 남은 자투리 거리가 지금 우주선이 이동할 수 있는 거리보다
    # 큰 경우, 현재 숫자값으로 해결할 수 없기 때문에 숫자값 + 1을 한 값을
    # 2배 해줌
    elif k > tmpI + 1:
        tmpI = (tmpI+1) * 2

    # 나머지 경우에는 현재 이루고 있는 대칭값을 구해주고(tmpI * 2),
    # 이 값에 1을 더해줌
    else:
        tmpI = tmpI * 2 + 1
    
    print(tmpI)