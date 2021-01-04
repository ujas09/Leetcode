class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        deliciousness.sort()

        power_2 = [2 ** i for i in range(22)]

        counter = {}
        result = 0
        for num in deliciousness:

            for i in range(0, len(power_2)):
                if power_2[i] >= num:
                    if power_2[i] - num in counter:
                        result += counter[power_2[i] - num]
                        result %= 1000000007
            counter[num] = counter.get(num, 0) + 1

        return result % 1000000007