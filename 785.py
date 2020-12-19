class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color = [-1] * len(graph)
        visited = [0] * len(graph)

        for i in range(0, len(graph)):
            if not visited[i]:
                stk = [i]
                color[i] = 0
                now_color = 0
                visited[i] = 1
                while stk:

                    tem = []
                    now_color ^= 1
                    while stk:
                        node = stk.pop()

                        for next_node in graph[node]:
                            visited[next_node] = 1
                            if color[next_node] == -1:
                                color[next_node] = now_color
                                tem.append(next_node)
                            else:

                                if color[next_node] != now_color:
                                    return False
                    stk = tem

        return True


