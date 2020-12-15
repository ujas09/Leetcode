class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if m * k > len(arr):
            return False

        def helper(start, arr, m, k):

            for i in range(0, k - 1):
                for j in range(0, m):
                    if arr[start + i * m + j] != arr[start + (i + 1) * m + j]:
                        return False

            return True

        for i in range(0, len(arr) - m * k + 1):
            if helper(i, arr, m, k):
                return True
        return False