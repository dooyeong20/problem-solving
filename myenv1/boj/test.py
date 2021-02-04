from sys import stdin

def trade_bnp(bnp, price):
    cnt = bnp[0] // price
    if not cnt:
        return

    bnp[0] -= price * cnt
    bnp[1] = cnt

def trade_timing(timing, flag, price):
    if flag > 0:
         cnt = timing[0] // price
         if not cnt:
             return

         timing[0] -= price * cnt
         timing[1] += cnt
    else:
        if not timing[1]:
            return
        timing[0] += price * timing[1]
        timing[1] = 0

amount = int(input())
prices = list(map(int, stdin.readline().split()))

bnp = [amount, 0]
timing = [amount, 0]
rise = 0
fall = 0

for i in range(14):
    trade_bnp(bnp, prices[i])

    if i == 0:
        continue

    if prices[i-1] < prices[i]:
        rise += 1
        fall = 0
    elif prices[i-1] > prices[i]:
        rise = 0
        fall += 1
    else:
        rise = 0
        fall = 0
    
    if rise >= 3:
        trade_timing(timing, -1, prices[i])
    elif fall >= 3:
        trade_timing(timing, 1, prices[i])
    

bnpTotal = bnp[0] + bnp[1] * prices[-1]
timingTotal = timing[0] + timing[1] * prices[-1]

if bnpTotal < timingTotal:
    print('TIMING')
elif bnpTotal > timingTotal:
    print('BNP')
else:
    print('SAMESAME')