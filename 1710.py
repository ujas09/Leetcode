class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        units = 0
        boxTypes.sort(key=lambda x: x[1])
        while truckSize and boxTypes:
            nB, nU = boxTypes.pop()

            taken_box = min(truckSize, nB)

            units += taken_box * nU

            truckSize -= taken_box

        return units