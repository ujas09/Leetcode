# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        # make a dummy node to handle if all the node is duplicate
        result = ListNode(-1)

        # add the total head in the next
        result.next = head

        # track how long the nodes are unique
        privious = result

        while head:

            # if finds duplicates
            if head.next and head.val == head.next.val:

                while head.next and head.val == head.next.val:
                    head = head.next

                # remove the duplicates
                privious.next = head.next
            else:
                # if no duplicates moved the next node
                privious = privious.next

            # move the head also
            head = head.next

        return result.next


