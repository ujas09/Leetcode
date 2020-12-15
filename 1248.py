class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        result = 0
        start = 0

        count_num = 0
        odd = 0
        for i in range(0, len(nums)):
            if nums[i] % 2 == 1:
                odd += 1
                count_num = 0
            while odd == k:

                if nums[start] % 2 == 1:
                    odd -= 1
                start += 1
                count_num += 1

            result += count_num

        return result
