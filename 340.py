class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        left = 0
        right = 0
        counter = {}
        length = len(s)
        result = 0
        while right < length:
            counter[s[right]] = counter.get(s[right], 0) + 1
            right += 1

            while len(counter.keys()) > k:
                counter[s[left]] = counter.get(s[left], 0) - 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1

            result = max(result, right - left)

        return result