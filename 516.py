class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        # Use dinamic programming to the result


        if len(s) == 0:
            return 0

        DP = [[0] * (len(s) + 1) for i in range(len(s) + 1)]

        reverse_s = s[::-1]

        #
        for i in range(1, len(s) + 1):
            for j in range(1, len(s) + 1):

                # if the char in string and reverse string is same
                if s[i - 1] == reverse_s[j - 1]:
                    DP[i][j] = DP[i - 1][j - 1] + 1

                else:
                    DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

        return DP[-1][-1]

