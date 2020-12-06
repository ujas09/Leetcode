class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        vertical_area = 0
        points.sort()
        for i in range(0, len(points) - 1):
            vertical_area = max(vertical_area, points[i + 1][0] - points[i][0])

        return vertical_area