class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        # make an prefix sum arr
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        # handle one edge case
        if nums[-1] == nums[0]:
            return 0

        # search the pivot that satisfy the logic
        for i in range(1, len(nums)):
            if nums[i - 1] * 2 + (nums[i] - nums[i - 1]) == nums[-1]:
                return i

        # if not find anything return -1
        return -1