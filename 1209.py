class Solution:
    def removeDuplicates(self, string: str, k: int) -> str:

        # make a stack to track the character and count of character
        stk = []

        for s in string:

            # if the stack is empty add the char with count 1
            if len(stk) == 0:
                stk.append([s, 1])

            else:
                # pop the last char with count
                char, count = stk.pop()

                # if s and the last char is same upgreat the count and add again
                if char == s:
                    count += 1
                    # if count is k don't add
                    if count != k:
                        stk.append([char, count])
                else:

                    # if they are not same add both char in stack
                    stk.append([char, count])
                    stk.append([s, 1])

        # construct the result

        result = ''

        # went through the stack and construct the result
        for i in range(0, len(stk)):
            result += stk[i][0] * stk[i][1]

        return result