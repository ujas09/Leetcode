class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        target = sum(stones) // 2
        DP = [1] + [0] * target
        stones.sort()

        for i in range(0, len(stones)):
            for j in range(target, -1, -1):
                if DP[j] and j + stones[i] <= target:
                    DP[j + stones[i]] = 1
                    # if DP[target]:
                    #     return sum(stones) - target*2

        for i in range(target, -1, -1):
            if DP[i]:
                return sum(stones) - i * 2


