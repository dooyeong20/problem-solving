from itertools import combinations as combi


def solution(info, query):
    answer = []
    combiDict = {}

    for i in info:
        tmpInfo = i.split(' ')
        val = int(tmpInfo[-1])
        tmpInfo = tmpInfo[:-1]

        for i in range(5):
            for c in combi(tmpInfo, i):
                if c not in combiDict:
                    combiDict[c] = []

                combiDict[c].append(val)

    for d in combiDict:
        combiDict[d].sort()

    for q in query:
        cnt = 0
        q = [c for c in q.split(' ') if c != 'and' and c != '-']
        val = int(q.pop())
        q = tuple(q)

        if q not in combiDict:
            answer.append(cnt)
            continue

        arr = combiDict[q]
        length = len(arr)
        st, en = 0, length - 1

        while st <= en:
            mid = (st+en)//2

            if arr[mid] < val:
                st = mid + 1
            else:
                en = mid - 1
        idx = en + 1

        answer.append(length-idx)

    return answer
