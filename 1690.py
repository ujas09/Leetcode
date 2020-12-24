class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        DP = [[0] * n for i in range(n)]
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + stones[i])

        def helper(start, end, stones):
            if start == end:
                return 0
            if DP[start][end]:
                return DP[start][end]
            sumation = prefix[end + 1] - prefix[start]
            ans = max(sumation - stones[start] - helper(start + 1, end, stones),
                      sumation - stones[end] - helper(start, end - 1, stones))

            DP[start][end] = ans

            return ans

        return helper(0, len(stones) - 1, stones)
