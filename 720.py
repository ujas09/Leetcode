class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        result = ''

        # track the words who is possible from the sorted words
        track = {'': 1}

        # go every word and check it is possible to make one character at a time by other words
        for word in words:
            if word[:-1] in track:
                track[word] = 1

                # if fond solution is bigger than the existing solution
                if len(word) > len(result):
                    result = word
                # if same length select the smallest
                elif len(result) == len(word):
                    result = min(result, word)

        return result
