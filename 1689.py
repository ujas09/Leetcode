class Solution:
    def minPartitions(self, n: str) -> int:
        result = 0

        for num in n:
            result = max(result, int(num))

        return result
