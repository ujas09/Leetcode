class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        tracker = {}

        for i in range(0, len(target)):
            tracker[target[i]] = i

        tem = []

        for i in range(0, len(arr)):
            if arr[i] in tracker:
                tem.append(tracker[arr[i]])
        result = []
        for i in range(0, len(tem)):
            index = bisect.bisect_left(result, tem[i])

            if index == len(result):
                result.append(tem[i])
            else:
                result[index] = tem[i]
        return len(target) - len(result)