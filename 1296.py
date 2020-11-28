class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # check the edge case (Can we divide the list into k groups or not)
        if len(nums) % k != 0: return False
        # make a counter to count the number of same type of cards
        counter = {}
        # populate the counter
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        # start the searching from the first available point
        for key in sorted(counter):

            if counter[key]:
                value = counter[key]
                # check that can we make k consecutive cards or not
                for i in range(k):
                    counter[key + i] = counter.get(key + i, 0) - value

                    if counter[key + i] < 0:
                        return False
        # if we are here it is possible
        return True
