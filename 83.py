# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # consider the edge case
        if head == None or head.next == None:
            return head

        # assign the result
        result = head

        first = head
        while first.next:
            second = first.next
            # if found the duplicate delete the second
            if first.val == second.val:
                first.next = first.next.next
            else:
                first = second

        return result

