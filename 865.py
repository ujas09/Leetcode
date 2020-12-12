# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def add_height(node):
            if node == None:
                return 0
            left = add_height(node.left)
            right = add_height(node.right)

            node.height = max(left, right) + 1
            return node.height

        head = root
        add_height(root)

        while head:
            if not head.left and not head.right:
                return head
            if not head.left:
                head = head.right
            elif not head.right:
                head = head.left
            elif head.left.height == head.right.height:
                return head

            elif head.left.height > head.right.height:
                head = head.left
            else:
                head = head.right

        return root

