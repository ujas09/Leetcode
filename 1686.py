class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:

        arr = []

        for i in range(0, len(aliceValues)):
            arr.append([aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i]])
        arr.sort(reverse=True)

        alice = 0
        bob = 0

        for i in range(0, len(arr)):
            if i % 2 == 0:
                alice += arr[i][1]
            else:
                bob += arr[i][2]
        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        return 0
