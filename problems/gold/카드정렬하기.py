 from sys import stdin
  import heapq

   def solution(n, cards):
        if n == 1:
            return 0

        heapq.heapify(cards)

        ans = 0
        tmp = []

        while n > 1:
            tmp = heapq.heappop(cards) + heapq.heappop(cards)
            ans += tmp
            heapq.heappush(cards, tmp)
            n -= 1

        return ans

    n = int(input())
    cards = [int(stdin.readline()) for _ in range(n)]

    print(solution(n, cards))
