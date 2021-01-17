class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = {}
        nums.sort()
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                counter[nums[i] * nums[j]] = counter.get(nums[i] * nums[j], 0) + 1

        result = 0

        for key in counter.keys():
            result += ((counter[key] - 1) * (counter[key]) // 2) * 8

        return result