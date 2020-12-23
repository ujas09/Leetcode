import heapq


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        steps = [1] * len(arr)

        min_heap = []

        for i in range(0, len(arr)):
            heapq.heappush(min_heap, [arr[i], i])

        while min_heap:
            value, index = heapq.heappop(min_heap)

            tem = 1

            for i in range(index + 1, min(len(arr) - 1, index + d) + 1):
                if value > arr[i]:
                    tem = max(tem, 1 + steps[i])
                else:
                    break
            for i in range(index - 1, max(0, index - d) - 1, -1):
                if value > arr[i]:
                    tem = max(tem, 1 + steps[i])
                else:
                    break
            steps[index] = max(steps[index], tem)

        return max(steps)

