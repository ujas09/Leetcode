class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])

        arr = [[] for i in range(m + n - 1)]

        for i in range(m):
            for j in range(n):
                arr[i + j].append(matrix[i][j])
        result = []
        for i in range(0, len(arr)):
            if i % 2 == 1:
                for j in range(0, len(arr[i])):
                    result.append(arr[i][j])
            else:
                for j in range(len(arr[i]) - 1, -1, -1):
                    result.append(arr[i][j])
        return result

