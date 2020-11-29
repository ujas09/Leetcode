class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # handle the base case
        if len(nums) == 0: return 0

        # Sort the arr
        nums.sort()

        # store the number we saw and used or not
        tracknumbers = {}

        # store thr result
        result = 0
        for num in nums:

            # check the num - k is in dictionary and we can use or not
            if num - k in tracknumbers and tracknumbers[num - k]:
                result += 1
                # make the number used
                tracknumbers[num - k] = 0

            # if we not added the number
            if num not in tracknumbers:
                tracknumbers[num] = 1

        # return the result
        return result
