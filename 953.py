class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # make a priority dictionary to store the order for future O(1) call
        priority = {}

        # populate the dictionary
        for i in range(0, len(order)):
            priority[order[i]] = i

        # check the two consecutive is assecding or not
        for i in range(0, len(words) - 1):
            conflict = True
            for j in range(0, min(len(words[i]), len(words[i + 1]))):

                if priority[words[i][j]] < priority[words[i + 1][j]]:
                    conflict = False
                    break
                elif priority[words[i][j]] > priority[words[i + 1][j]]:
                    return False
            # if both thw words have similar prefix than length is the factor
            if conflict and len(words[i]) > len(words[i + 1]):
                return False
        return True
