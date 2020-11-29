class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        # used the top down approch to calculate the smallest prefixsum for every row in the matrix

        # if the matrix is 1*1
        if len(A) == 1:
            return A[0][0]

        N = len(A[0])

        for i in range(1, len(A)):
            for j in range(0, N):
                # if we are in first position of a row, there is only two point from the previous row we can come
                if j == 0:
                    A[i][j] += min(A[i - 1][j], A[i - 1][j + 1])
                # if we are in last position of a row, there is only two point from the previous row we can come
                elif j == N - 1:
                    A[i][j] += min(A[i - 1][j], A[i - 1][j - 1])
                    # other than we have three points
                else:
                    A[i][j] += min(A[i - 1][j], A[i - 1][j + 1], A[i - 1][j - 1])
        return min(A[-1])