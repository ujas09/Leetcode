class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # store the result
        result = []
        # store the scores for each Id
        scores = {}

        for id, score in items:
            scores[id] = scores.get(id, []) + [score]

        # get the IDs in decending orders and get the avg for the highest 5 numbers
        for id in sorted(scores):
            scores[id].sort(reverse=True)

            result.append([id, sum(scores[id][:5]) // 5])
        # return the avg scores
        return result
