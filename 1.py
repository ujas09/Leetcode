class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create an dictionary
        nummap={}
        for i in range(0,len(nums)):
            # check the target already we can make it or not
            n=target-nums[i]
            # if target - number is in dictionary we found the solution
            if n not in nummap:
                nummap[nums[i]]=i
            else:
                return[nummap[n],i]