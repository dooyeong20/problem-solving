def solution(n, times):
    def check(totalTime):
        cnt = 0

        for t in times:
            cnt += totalTime // t

        return cnt

    ans = 0
    st, en = 1, 1000000000000000000

    while st <= en:
        mid = (st + en) // 2

        if check(mid) >= n:
            en = mid - 1
        else:
            st = mid + 1

    return en + 1
