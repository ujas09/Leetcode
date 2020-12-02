class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        n = len(jobDifficulty)

        if n < d:
            return -1
        from functools import lru_cache
        @lru_cache(None)
        def dp(start, end, day):
            if day == 1:
                return max(jobDifficulty[start:end])

            element = []
            for i in range(start + 1, end):
                element.append(max(jobDifficulty[start:i]) + dp(i, end, day - 1))

            if len(element) == 0:
                return 1000000000

            return min(element)

        return dp(0, n, d)