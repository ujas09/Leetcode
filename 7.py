class Solution:
    def reverse(self, x: int) -> int:
        # make a flag to check negative or positive
        flag = 0

        # check the negative value
        if x < 0:
            flag = 1
            x = -1 * x

        # this is the return value
        result = 0

        # reverse the integer
        while (x > 0):
            result = result * 10 + x % 10
            x = x // 10

        # Change the result for negative
        if flag:
            result = -1 * result
            if result >= -1 * 2 ** 31:
                return result
            else:
                return 0
        # Return the result for positive
        if result < 2 ** 31:
            return result
        else:
            return 0

