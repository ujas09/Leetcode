class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        row = len(dungeon)
        col = len(dungeon[0])
        DP = [[-1 * sys.maxsize] * col for i in range(row)]

        def helper(r, c):

            if row <= r or col <= c:
                return -1 * sys.maxsize
            if DP[r][c] != -1 * sys.maxsize:
                return DP[r][c]
            if r == row - 1 and c == col - 1:
                return 0 if dungeon[r][c] >= 0 else dungeon[r][c]
            ans = max(helper(r + 1, c), helper(r, c + 1))

            if ans + dungeon[r][c] >= 0:
                DP[r][c] = 0
                return 0
            DP[r][c] = ans + dungeon[r][c]
            return ans + dungeon[r][c]

        return abs(helper(0, 0)) + 1