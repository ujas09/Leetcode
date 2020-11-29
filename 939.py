class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        # make a dictionary to store the points for O(1) search
        pointset = {}

        for i in range(0, len(points)):
            pointset[(points[i][0], points[i][1])] = 1

        result = float('inf')

        # took two diagonal point and look at the other points are in points or not. if the other points are present calculate the area
        for i in range(0, len(points) - 1):
            for j in range(i + 1, len(points)):

                if points[i][0] != points[j][0] and points[i][1] != points[j][1] and (
                points[i][0], points[j][1]) in pointset and (points[j][0], points[i][1]) in pointset:
                    result = min(result, abs(points[i][0] - points[j][0]) * abs(points[j][1] - points[i][1]))

        return result if result != float('inf') else 0