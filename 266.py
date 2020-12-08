class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        palindom = False

        for key in char_count.keys():
            if char_count[key] % 2 == 1:
                if palindom:
                    return False
                palindom = True

        return True