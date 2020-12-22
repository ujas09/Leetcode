# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def hightcal(root):

            if not root:
                return 0, True

            leftheight, leftbalance = hightcal(root.left)
            if not leftbalance:
                return 0, False
            rightheight, rightbalance = hightcal(root.right)
            if not rightbalance:
                return 0, False

            return max(leftheight, rightheight) + 1, abs(leftheight - rightheight) < 2

        if not root:
            return True

        return hightcal(root)[1]