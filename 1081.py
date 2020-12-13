class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_index = {}

        for i in range(0, len(s)):
            last_index[s[i]] = i

        stk = []
        used = {}
        for i in range(0, len(s)):
            if s[i] not in used:
                while stk and stk[-1] > s[i] and last_index[stk[-1]] > i:
                    del used[stk.pop()]
                stk.append(s[i])
                used[s[i]] = 1

        return "".join(stk)