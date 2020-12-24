class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        DP = [-1 * (sys.maxsize)] * n

        if n >= 1:
            DP[-1] = stoneValue[-1]
        DP.append(0)
        for i in range(n - 2, -1, -1):
            DP[i] = max([sum(stoneValue[i:j]) - DP[j] for j in range(i + 1, min(i + 4, n + 1))])

        if DP[0] == 0:
            return 'Tie'
        return 'Alice' if DP[0] > 0 else 'Bob'
