import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        result = 0
        next_station = []
        heapq.heapify(next_station)

        index = 0
        while startFuel < target:

            if index >= len(stations) or stations[index][0] > startFuel:
                if len(next_station) == 0:
                    return -1
                startFuel += (-1 * heapq.heappop(next_station))
                result += 1
            else:

                heapq.heappush(next_station, -1 * stations[index][1])
                index += 1
        return result
