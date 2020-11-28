class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # count the number od times saw a specific number
        counter = {}
        result = 0

        for t in time:
            remaining = 60 - (t % 60)
            # check how many solution posssible from past times
            if remaining % 60 in counter:
                result += counter[remaining % 60]
            counter[t % 60] = counter.get(t % 60, 0) + 1

        return result
