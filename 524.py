class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def check(tem1, tem2):
            j = 0
            for i in range(0, len(tem1)):
                if tem1[i] == tem2[j]:
                    j += 1
                if j == len(tem2):
                    return True
            return False

        d.sort(key=lambda x: [-len(x), x])

        for i in range(0, len(d)):
            if check(s, d[i]):
                return "".join(d[i])

        return ""
