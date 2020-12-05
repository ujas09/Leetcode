# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root:
                inorder(root.left)
                self.head.right = TreeNode(root.val)
                self.head = self.head.right

                inorder(root.right)

        result = TreeNode()

        self.head = result

        inorder(root)

        return result.right