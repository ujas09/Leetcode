class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:

        # store the results in 2-d list
        DP = [[0] * N for i in range(N)]

        DP[r][c] = 1

        # for every move calculates the probability in tem 2-d list
        for i in range(0, K):
            tem = [[0] * N for i in range(N)]

            for r in range(0, N):
                for c in range(0, N):

                    # select the one of eight possible moves
                    for dr, dc in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]:
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            # divided the value by 8 as it can move 8 direction
                            tem[r + dr][c + dc] += DP[r][c] / 8

            # Store the list in DP
            DP = tem

        result = 0

        # add the values in DP
        for r in range(N):
            result += sum(DP[r])

        return result

