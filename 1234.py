class Solution:
    def balancedString(self, s: str) -> int:

        n = len(s) // 4

        counter = {}

        expected = {}

        # make a counter for every char
        for char in s:
            counter[char] = counter.get(char, 0) + 1

        # make an expected dictionary that we needs to change
        for key in counter.keys():

            if counter[key] > n:
                expected[key] = counter[key] - n

        if len(expected) == 0:
            return 0

        # Find the smallest length of substring that fullfil the expected dic
        start = 0
        result = len(s)
        for j in range(0, len(s)):
            if s[j] in expected:
                expected[s[j]] -= 1

            while max(expected.values()) <= 0:
                result = min(result, j - start + 1)

                if s[start] in expected:
                    expected[s[start]] += 1
                start += 1

        return result

