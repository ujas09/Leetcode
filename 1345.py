class Solution:
    def minJumps(self, arr: List[int]) -> int:
        counter = {}
        visited = [False] * len(arr)
        for i in range(0, len(arr)):
            if arr[i] in counter:
                counter[arr[i]].append(i)
            else:
                counter[arr[i]] = [i]

        result = 0
        stk = [0]
        visited[0] = True
        target = len(arr) - 1
        while stk:
            tem = []

            while stk:
                node = stk.pop()

                if node == target:
                    return result

                if node - 1 >= 0 and not visited[node - 1]:
                    tem.append(node - 1)
                    visited[node - 1] = True
                if node + 1 <= target and not visited[node + 1]:
                    tem.append(node + 1)
                    visited[node + 1] = True
                while counter[arr[node]]:
                    next_node = counter[arr[node]].pop()
                    if not visited[next_node]:
                        tem.append(next_node)
                        visited[next_node] = True
            stk = tem
            result += 1
        return -1
