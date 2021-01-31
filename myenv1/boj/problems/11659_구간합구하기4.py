from sys import stdin

n , m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
calNums = []
tmp = 0

for n in nums:
    tmp += n
    calNums.append(tmp)


for _ in range(m):
    st, en = map(int, stdin.readline().split())
    ans = calNums[en-1]

    if st > 1:
        ans -= calNums[st-2]
    
    print(ans)
