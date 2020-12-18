class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefixsum = {-1: 0}

        for i in range(0, len(nums)):
            prefixsum[i] = prefixsum[i - 1] + nums[i]

        result = []
        n = len(nums)
        for i in range(0, len(nums)):
            result.append(
                abs(prefixsum[i] - (i + 1) * nums[i]) + abs(prefixsum[n - 1] - prefixsum[i] - (n - 1 - i) * nums[i]))

        return result