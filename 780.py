class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # start feom the target and check that we can achive the start point or not


        # terminate the while loop if tx or ty is less than the start point x and y
        while tx >= sx and ty >= sy:

            # True condition
            if tx == sx and ty == sy:
                return True

            # if tx greater than ty we know we need to subtract the ty from tx (so we took remainder to omite multiple subtraction)
            # sample test:(3, 3, 12, 9) if anytime ty == sy we only need to check (tx - sx) % ty == 0 or not
            # same thing for if tx == sx
            if tx > ty:
                if ty == sy:
                    return (tx - sx) % ty == 0
                tx = tx % ty
            else:
                if tx == sx:
                    return (ty - sy) % tx == 0
                ty = ty % tx
        # if we are out of while loop that means not possible
        return False