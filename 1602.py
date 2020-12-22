# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        found = False

        if root == u:
            return None
        stk = [root]

        while stk:
            tem = []
            while stk:
                node = stk.pop()
                if node.left:
                    if found:
                        return node.left
                    if node.left.val == u.val:
                        found = True
                    tem.append(node.left)
                if node.right:
                    if found:
                        return node.right
                    if node.right.val == u.val:
                        found = True
                    tem.append(node.right)

            stk = tem
            stk.reverse()
            found = False
        return None

