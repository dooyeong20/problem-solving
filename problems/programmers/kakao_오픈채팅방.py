def solution(record):
    ans = []
    nameDict = {}
    i = 0

    for r in record:
        r = r.split(' ')

        if r[0] == 'Enter':
            ans.append(1)
            uid, name = r[1], r[2]

            if uid not in nameDict:
                nameDict[uid] = [name, [i]]
            else:
                nameDict[uid][0] = name
                nameDict[uid][1].append(i)

        elif r[0] == 'Leave':
            ans.append(0)
            uid = r[1]
            nameDict[uid][1].append(i)

        else:
            uid, name = r[1], r[2]
            nameDict[uid][0] = name
            i -= 1

        i += 1

    for k in nameDict:
        name, idxList = nameDict[k]

        for idx in idxList:
            if ans[idx] > 0:
                ans[idx] = f'{name}님이 들어왔습니다.'
            else:
                ans[idx] = f'{name}님이 나갔습니다.'

    return ans


print(solution(['Enter 1 kim', 'Change 1 lee', 'Leave 1']))
