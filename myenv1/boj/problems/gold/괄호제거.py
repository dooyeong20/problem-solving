from sys import stdin

# 식과 인덱스가 주어지면 해당 인덱스의 괄호에 해당하는
# 괄호 한 쌍을 삭제한 식을 string 으로 반환해준다.
def get_tmp_exp(exp, x):
    s = []
    res = ''

    for i, e in enumerate(exp):
        if e == '(':
            s.append((e, i))
            if i == x:
                continue
        elif e == ')':
            if s[-1][1] == x:
                s.pop()
                continue

            s.pop()
            
        res += e
    
    return res

# 식을 재귀적인 방식으로 각각의 괄호쌍이 제거된 상태에 따라서
# 올바르게 괄호 한 쌍이 제거된 식을 expSet 에 저장한다.
def solve(exp):
    for i, e in enumerate(exp):
        if e == '(':
            tmpExp = get_tmp_exp(exp, i)

            # 불필요한 재귀 호출을 막기 위한 분기처리이다.
            if tmpExp not in expSet:
                expSet.add(tmpExp)
                solve(tmpExp)

# 재귀의 중복 탐색을 막기 위한 자료구조
expSet = set()
expStr = stdin.readline().strip()

solve(expStr)

print('\n'.join(sorted(list(expSet))))