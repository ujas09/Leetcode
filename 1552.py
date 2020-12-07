class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def placement(force, m):
            place_ball = 1

            next_pos = position[0] + force

            for i in range(1, len(position)):

                if position[i] >= next_pos:
                    place_ball += 1
                    next_pos = position[i] + force

                if place_ball == m:
                    return True
            return False

        position.sort()

        low = 0

        high = (position[-1] - position[0]) // (m - 1) + 1

        if m == 2:
            return high - 1

        while low <= high:

            mid = low + (high - low) // 2

            if placement(mid, m):
                low = mid + 1

            else:
                high = mid - 1

        return low - 1
