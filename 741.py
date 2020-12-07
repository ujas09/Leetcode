class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        DP = [[[-1] * n for i in range(n)] for j in range(n)]

        def calculate(r1, c1, c2):

            r2 = r1 + c1 - c2

            if r1 >= n or r2 >= n or c1 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -500

            if r2 == n - 1 and c2 == n - 1:
                return grid[r2][c2]
            if DP[r1][c1][c2] != -1:
                return DP[r1][c1][c2]

            ans = grid[r1][c1]

            if c1 != c2:
                ans += grid[r2][c2]

            ans += max(calculate(r1, c1 + 1, c2 + 1), calculate(r1, c1 + 1, c2), calculate(r1 + 1, c1, c2 + 1),
                       calculate(r1 + 1, c1, c2))
            DP[r1][c1][c2] = ans
            return ans

        return max(0, calculate(0, 0, 0))