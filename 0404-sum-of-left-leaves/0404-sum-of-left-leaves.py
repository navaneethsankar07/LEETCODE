# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0 
            
            sum = 0

            if node.left:
                if node.left.left is None and node.left.right is None:
                    sum += node.left.val
            
            sum += dfs(node.left)
            sum += dfs(node.right)

            return sum

        return dfs(root)       