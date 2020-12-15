class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def palindom(s):
            for i in range(0, len(s) // 2):
                if s[i] != s[-i - 1]:
                    return False
            return True

        def dfs(string, tem_result):

            if string == "":
                result.append(tem_result)

            for length in range(1, len(string) + 1):
                if palindom(string[:length]):
                    dfs(string[length:], tem_result + [string[:length]])
            return

        dfs(s, [])
        return result
