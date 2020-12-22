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
                return 0
            root.height = 1 + max(hightcal(root.left), hightcal(root.right))

            return root.height

        if not root:
            return True

        return abs(hightcal(root.left) - hightcal(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(
            root.right)