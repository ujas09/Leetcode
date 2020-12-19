class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        DP = [[[0] * n for i in range(n)] for j in range(m)]

        for row in range(m - 1, -1, -1):
            for col1 in range(0, n):
                for col2 in range(0, n):

                    DP[row][col1][col2] = grid[row][col1]

                    if col1 != col2:
                        DP[row][col1][col2] += grid[row][col2]

                    if row != m - 1:
                        DP[row][col1][col2] += max(DP[row + 1][new_col1][new_col2]
                                                   for new_col1 in [col1, col1 + 1, col1 - 1]
                                                   for new_col2 in [col2, col2 + 1, col2 - 1]
                                                   if 0 <= new_col1 < n and 0 <= new_col2 < n)

        # print(DP)

        return DP[0][0][n - 1]