from sys import stdin


def solution(brackets):
    ans = 0
    s = []

    for b in brackets:
        if b == '(' or b == '[':
            s.append(b)
            continue

        if b == ')':
            cur = 0

            while s:
                if s[-1] == '[':
                    return 0

                if s[-1] == '(':
                    s.pop()
                    s.append(cur*2 if cur else 2)
                    break

                cur += s.pop()
            else:
                return 0

            continue

        if b == ']':
            cur = 0

            while s:
                if s[-1] == '(':
                    return 0

                if s[-1] == '[':
                    s.pop()
                    s.append(cur*3 if cur else 3)
                    break

                cur += s.pop()
            else:
                return 0

    while s:
        tmp = s.pop()
        if tmp == '(' or tmp == '[':
            return 0

        ans += tmp

    return ans


brackets = stdin.readline().strip()
print(solution(brackets))
