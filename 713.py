class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        left = 0
        right = 0
        product = 1
        result = 0
        while right < len(nums):
            product *= nums[right]
            right += 1
            # print(left, right, product)
            if product >= k:
                while product >= k and left < right:
                    product = product // nums[left]
                    left += 1
            result += (right - left)

        return result