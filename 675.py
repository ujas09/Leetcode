import heapq


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:

        m = len(forest)

        n = len(forest[0])
        if forest[0][0] == 0:
            return -1

        def bfs(startx, starty, endx, endy):

            seen = {(startx, starty): 1}

            path = 0

            stk = [(startx, starty)]

            while stk:
                tem = []

                while stk:
                    nodex, nodey = stk.pop()
                    if nodex == endx and nodey == endy:
                        return path
                    for next_nodex, next_nodey in [(nodex + 1, nodey), (nodex - 1, nodey), (nodex, nodey + 1),
                                                   (nodex, nodey - 1)]:
                        if 0 <= next_nodex < m and 0 <= next_nodey < n and forest[next_nodex][next_nodey] and (
                        next_nodex, next_nodey) not in seen:
                            tem.append((next_nodex, next_nodey))
                            seen[(next_nodex, next_nodey)] = 1
                stk = tem
                path += 1

            return -1

        result = 0

        arr = []

        for i in range(0, m):
            for j in range(0, n):
                if forest[i][j]:
                    heapq.heappush(arr, (forest[i][j], i, j))
        startx, starty = 0, 0

        while arr:
            _, endx, endy = heapq.heappop(arr)
            dis = bfs(startx, starty, endx, endy)
            if dis == -1:
                return -1
            result += dis
            startx, starty = endx, endy
        return result


