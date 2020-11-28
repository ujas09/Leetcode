class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # check the edge case (Can we divide the list into W groups or not)
        if len(hand) % W != 0: return False

        # make a counter to count the number of same type of cards
        counter = {}

        # populate the counter
        for h in hand:
            counter[h] = counter.get(h, 0) + 1

        # start the searching from the first available point
        for key in sorted(counter):

            if counter[key]:
                value = counter[key]
                # check that can we make W consecutive cards or not
                for i in range(W):
                    counter[key + i] = counter.get(key + i, 0) - value

                    if counter[key + i] < 0:
                        return False

        # if we are here it is possible
        return True

