class Solution:
    # reverse the list from start point to end point
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]

            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # handle the case if k is greater than length of nums
        k = k % len(nums)

        # reverse the total list
        self.reverse(nums, 0, len(nums) - 1)

        # reverse the first k element
        self.reverse(nums, 0, k - 1)

        # reverse the last elements
        self.reverse(nums, k, len(nums) - 1)