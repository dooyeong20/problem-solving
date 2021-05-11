class Solution:
    def partitionLabels(self, s: str):
        sten = dict()
        ans = []

        for i in range(len(s)):
            if s[i] not in sten:
                sten[s[i]] = [i, -1]
            else:
                sten[s[i]][1] = i

        i = 0

        while i < len(s):
            tmp = sten[s[i]][1]
            j = i+1

            while j < tmp:
                if sten[s[j]][1] > tmp:
                    tmp = sten[s[j]][1]

                j += 1

            if tmp < 0:
                ans.append(1)
                i += 1
            else:
                ans.append(tmp - sten[s[i]][0] + 1)
                i = tmp + 1

        return ans
