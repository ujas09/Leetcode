import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        heapq.heapify(sticks)

        for i in range(0, len(sticks) - 1):
            next_stick = heapq.heappop(sticks) + heapq.heappop(sticks)

            cost += next_stick

            heapq.heappush(sticks, next_stick)

        return cost

