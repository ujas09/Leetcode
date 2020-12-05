import heapq

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        free_times = []
        schedules = []
        heapq.heapify(schedules)

        for i in range(0, len(schedule)):
            for j in range(0, len(schedule[i])):
                heapq.heappush(schedules, (schedule[i][j].start, schedule[i][j].end))

        start, end = heapq.heappop(schedules)

        while len(schedules):
            next_start, next_end = heapq.heappop(schedules)
            if next_start <= end:
                end = max(end, next_end)
            else:
                free_times.append(Interval(end, next_start))
                start = next_start
                end = next_end

        return free_times