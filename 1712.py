class Solution:
    def waysToSplit(self, nums: List[int]) -> int:

        result = 0

        prefix_sum = [0]

        for i in range(0, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        for i in range(1, len(prefix_sum) - 1):
            idx1 = bisect.bisect_left(prefix_sum, 2 * prefix_sum[i], i + 1, len(nums))

            idx2 = bisect.bisect_right(prefix_sum, prefix_sum[i] + (prefix_sum[-1] - prefix_sum[i]) // 2, i + 1,
                                       len(nums)) - 1

            result += max(0, idx2 - idx1 + 1)
        return result % 1000000007