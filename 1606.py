class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        req_handled = [0] * k

        requested = []

        before_serve_id = [i for i in range(k)]
        after_serve_id = []
        for i in range(0, len(arrival)):
            serve_id = i % k
            # print(requested)
            if serve_id == 0:
                after_serve_id = before_serve_id
                before_serve_id = []

            while requested and arrival[i] >= requested[0][0]:

                _, free = heapq.heappop(requested)

                if free >= serve_id:
                    heapq.heappush(after_serve_id, free)
                else:
                    heapq.heappush(before_serve_id, free)

            used = -1
            if after_serve_id:

                used = heapq.heappop(after_serve_id)
            elif before_serve_id:
                used = heapq.heappop(before_serve_id)
            else:
                continue

            req_handled[used] += 1
            heapq.heappush(requested, (arrival[i] + load[i], used))

        maximum = max(req_handled)

        return [i for i in range(0, len(req_handled)) if req_handled[i] == maximum]

