# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0

    def dfs(self, root, counter):
        if not root.left and not root.right:
            ones = 0
            counter[root.val] = counter.get(root.val, 0) + 1

            for key in counter.keys():
                if counter[key] % 2:
                    ones += 1
            if ones <= 1:
                self.result += 1
            counter[root.val] = counter.get(root.val, 0) - 1

            return
        counter[root.val] = counter.get(root.val, 0) + 1
        if root.left:
            self.dfs(root.left, counter)
        if root.right:
            self.dfs(root.right, counter)

        counter[root.val] = counter.get(root.val, 0) - 1
        return

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:

        self.dfs(root, {})

        return self.result
