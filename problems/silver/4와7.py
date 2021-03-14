from sys import stdin

# 시간복잡도를 위해서
# 2의 제곱승들을 미리 구해놓음
def get_powNums():
    res = dict()
    x = 1
    idx = 1
    tmp = 0

    while 1:
        tmp += 2*x
        if tmp > 1000000000:
            break
        res[idx] = tmp
        x *= 2
        idx += 1
    
    return res

# num와 해당하는 자리수를 재귀 함수를 통해 ans에 자리를 더해간다 
# (자리수가 1이 될때가 종료조건)
def get_answer(num , digit):
    global ans

    tmpNum = twoPows[digit]
    if num > tmpNum:
        num -= tmpNum
    
    if digit == 1:
        if num == 1:
            ans += '4'
        elif num == 2:
            ans += '7'

        return

    # 해당하는 재귀 부분에서 가장 앞 자리 수를 구하기 위해서
    # 자리수 - 1에서 4와 7로 만들 수 있는 수가 전체 수의 반보다 작거나 같다면
    # 가장 앞자리 수는 4이다.
    # 반대로, 전체 수의 반보다 크면 7이다.
    if num <= tmpNum // 2:
        ans += '4'
    else:
        ans += '7'
    
    get_answer(num, digit-1)

# 2, 4, 8, 16 ... 계속해서 진행되는 등비수열의 합을
# 구해서 저장한다.
def set_pows():
    tmp = 1

    while 1: 
        twoPows.append(tmp)
        tmp *= 2

        if tmp > 1000000000:
            break

powNums = get_powNums()
twoPows = []
n = int(input())
num = 0
di = 1
ans = ''

set_pows()

# 등비수열의 합들을 이용해 자리 수와 해당하는 자리수에서 몇 번째
# 수를 구해야하는지 num와 di에 저장한다.
for key, val in powNums.items():
    if n > val:
        num = powNums[di]
        di += 1
        continue
    break
    
n -= num

# get_answer를 통해 ans에 가장 앞자리 수부터 차례로 구해서 더해준다. 
get_answer(n, di)
print(ans)