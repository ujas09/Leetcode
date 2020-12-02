class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # store the past coins result in past and
        past = [0] * (amount + 1)
        past[0] = 1

        coins.sort()
        for coin in coins:
            # store the result if we add a new coin
            present = [1]
            for amt in range(1, amount + 1):
                if amt - coin >= 0:
                    present.append(present[-coin] + past[amt])
                else:
                    present.append(past[amt])
            # after execute for 1 to amount present will be past for next coin
            past = present

        return past[-1]