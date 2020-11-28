class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:

        # track the indexs for word1
        index1 = []

        for i in range(0, len(words)):
            if words[i] == word1:
                index1 += [i]

        # track the indexs for word2
        index2 = []
        for i in range(0, len(words)):
            if words[i] == word2:
                index2 += [i]
        # find the shortes distance
        return min(abs(i - j) for i in index1 for j in index2)

