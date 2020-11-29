class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # store the max meeting room requered on that time
        max_meetingrooms = 0

        # store the starting time and end time saparately and sorted
        start_time = sorted([i[0] for i in intervals])
        end_time = sorted([i[1] for i in intervals])

        # start both start and end on oth index
        start = 0
        end = 0

        # run as long as intervals
        while start < len(intervals):

            # if current start time is greater than oe equal to current end time one room is free incease end with 1 else we need one more room so start += 1
            if start_time[start] >= end_time[end]:
                end += 1
            else:
                start += 1

            # track the room requerment after every step
            max_meetingrooms = max(max_meetingrooms, start - end)

        return max_meetingrooms

