class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        # find the remainder for the total summation
        total = sum(nums)

        remainder = total % p

        if remainder == 0:
            return 0

        result = float('inf')
        prefixsum = [0]
        seen = {0: -1}

        # did the prefixsum and find that we already saw the remainders or not if found calculate the subarray size
        for i in range(0, len(nums)):

            prefixsum.append(prefixsum[-1] + nums[i])

            rem = prefixsum[-1] % p
            # if it is in seen that means we found an solution
            if (rem - remainder) % p in seen:
                result = min(result, i - seen[(rem - remainder) % p])
            seen[rem] = i

        return result if result < len(nums) else -1


