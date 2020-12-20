class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)

        KMP = [0] * n

        start = 0

        for end in range(1, n):
            while s[start] != s[end] and start > 0:
                start = KMP[start - 1]
            if s[start] == s[end]:
                KMP[end] = start + 1
                start += 1
        return s[:KMP[-1]]
