class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0

        num_count = {}

        for num in nums:
            good_pairs += num_count.get(num, 0)

            num_count[num] = num_count.get(num, 0) + 1

        return good_pairs