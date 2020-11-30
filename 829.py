class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:

        # Calculate the upper limit from N

        upper_boundry = ceil((2 * N + 0.25) ** 0.5 - 0.5)

        result = 0
        for k in range(1, upper_boundry + 1):
            # check thatit is integer
            if (N - k * (k + 1) // 2) % k == 0:
                result += 1
        return result