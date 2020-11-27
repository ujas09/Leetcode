class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        # store the result
        result = []

        start = 0
        end = len(S)

        # for every char if it is 'I' store thr start value and increase else store thr end value and decrease the value
        for char in S:
            if char == 'I':
                result.append(start)
                start += 1
            else:
                result.append(end)
                end -= 1
        # last store the remaining value
        result.append(start)

        # return the result
        return result
