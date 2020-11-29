class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # handle the edge case
        if rowIndex == 0:
            return [1]
        # use only limited space to solve the problem
        past = [1]

        # past and present two list to solve the problem
        for row in range(0, rowIndex):
            present = [1] * (len(past) + 1)

            # calculate the present list from past
            for i in range(1, len(past)):
                present[i] = past[i] + past[i - 1]
            # store the present as past for next row
            past = present.copy()

        return past
