class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def check(b, a):
            if len(b) - len(a) != 1:
                return False

            i = j = 0
            cnt = 0

            while i < len(a):
                if a[i] != b[j]:
                    if cnt > 0:
                        return False

                    j += 1
                    cnt += 1
                    continue

                i += 1
                j += 1

            return True

        dp = [1] * len(words)
        ans = 1
        words.sort(key=lambda x: len(x))

        for i in range(1, len(words)):
            for j in range(i):
                if check(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])

        return(ans)
