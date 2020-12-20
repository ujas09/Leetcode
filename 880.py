class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:

        size = 0

        for string in S:
            if string.isdigit():
                size *= int(string)
            else:
                size += 1

        for i in range(len(S) - 1, -1, -1):
            K %= size

            if K == 0 and not S[i].isdigit():
                return S[i]

            if S[i].isdigit():
                size /= int(S[i])
            else:
                size -= 1
