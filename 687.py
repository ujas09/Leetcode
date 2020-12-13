# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        self.result = 0

        def helper(root):
            if root == None:
                return 0
            left = helper(root.left)
            right = helper(root.right)

            if root.left and root.val == root.left.val:
                left += 1
            else:
                left = 0
            if root.right and root.val == root.right.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)

            return max(left, right)

        helper(root)
        return self.result
