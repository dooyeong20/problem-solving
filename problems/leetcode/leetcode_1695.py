class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        used = [0] * 10001
        left, total, ans = 0, 0, 0

        for right in nums:
            total += right

            if not used[right]:
                used[right] = 1

            else:
                while used[right]:
                    total -= nums[left]
                    used[nums[left]] = 0
                    left += 1

                used[right] = 1

            ans = max(ans, total)

        return ans
