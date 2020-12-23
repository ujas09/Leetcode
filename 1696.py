class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        max_heap = []

        heapq.heappush(max_heap, [-nums[0], 0])

        DP = [0] * len(nums)

        DP[0] = nums[0]

        for i in range(1, len(nums)):
            while max_heap[0][1] < i - k:
                heapq.heappop(max_heap)

            DP[i] = DP[max_heap[0][1]] + nums[i]
            heapq.heappush(max_heap, [-DP[i], i])

        return DP[-1]

