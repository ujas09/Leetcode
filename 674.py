class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        length = 1
        tem_length = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                tem_length += 1
            else:
                length = max(length, tem_length)
                tem_length = 1

        length = max(length, tem_length)

        return length