class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = {}
        pairs = 0
        for i in arr:
            rem = i % k
            if rem in counter and counter[rem] > 0:
                pairs += 1
                counter[rem] -= 1
            else:
                reminder = (k - rem) % k
                counter[reminder] = counter.get(reminder, 0) + 1

        return pairs == len(arr) // 2
