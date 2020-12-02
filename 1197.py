class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        @lru_cache(None)
        def recursive(x, y):
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            return min(recursive(abs(x - 2), abs(y - 1)), recursive(abs(x - 1), abs(y - 2))) + 1

        return recursive(abs(x), abs(y))

# directions = [[-2,-1], [-2,1], [-1, -2], [-1, 2], [1,-2],[1,2],[2,-1],[2,1]]

#         stk = [[0,0]]

#         visited = {(0,0):1}

#         result = 0
#         while stk:
#             tem = []

#             while stk:
#                 node  = stk.pop()
#                 if node[0] == x and node[1] == y: return result
#                 for direction in directions:
#                     if (node[0] + direction[0], node[1] + direction[1]) not in visited:
#                         visited[(node[0] + direction[0], node[1] + direction[1])] = 1
#                         tem.append([node[0] + direction[0], node[1] + direction[1]])

#             stk = tem
#             result += 1



