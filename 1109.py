class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # store the result in list
        result = [0] * n

        # use the dictionary to trac how many additional seat needed on that fligts
        track = {}

        # calculated the needed seats
        for i in range(0, len(bookings)):
            track[bookings[i][0] - 1] = track.get(bookings[i][0] - 1, 0) + bookings[i][2]
            track[bookings[i][1]] = track.get(bookings[i][1], 0) - bookings[i][2]

        # assigning the prefix sum seats into the results
        totalseat = 0
        for i in range(0, n):
            totalseat += track.get(i, 0)
            result[i] = totalseat

        # return the result
        return result

