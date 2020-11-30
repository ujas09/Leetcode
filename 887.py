class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # Store the past calculated results
        result = {}

        # this function calculate the result
        def dp(k, n):
            if (k, n) not in result:
                # if no floor the number of eggs needed is zero
                if n == 0:
                    ans = 0
                # if I anly have one egg i need to try from every fall
                elif k == 1:
                    ans = n
                # if other need to search by using binary search
                else:
                    low = 1
                    high = n

                    while low + 1 < high:
                        mid = (low + high) // 2

                        value1 = dp(k - 1, mid - 1)
                        value2 = dp(k, n - mid)

                        if value1 < value2:
                            low = mid
                        elif value1 > value2:
                            high = mid
                        else:
                            low = mid
                            high = mid
                    # calculate the ans from high to low as we are following the diff atleast 2
                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x)) for x in (low, high))
                result[(k, n)] = ans
            return result[(k, n)]

        return dp(K, N)