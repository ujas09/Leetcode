class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = {}

        for num in arr:
            counter[num] = counter.get(num, 0) + 1

        hq = []

        for key in counter.keys():
            heapq.heappush(hq, -1 * counter[key])

        n = len(arr) // 2

        res = 0
        while n > 0:
            n -= (-1 * heapq.heappop(hq))
            res += 1

        return res