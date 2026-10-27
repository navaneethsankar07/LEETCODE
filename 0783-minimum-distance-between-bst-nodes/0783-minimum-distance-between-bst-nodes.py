# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        self.ans = float('inf')
        self.prev = None
        self.inorder(root)
        return self.ans
    
    def inorder(self, node):
        if not node:
            return
        
        self.inorder(node.left)

        if self.prev is not None:
            self.ans = min(self.ans, node.val - self.prev)
        
        self.prev = node.val

        self.inorder(node.right)
    

        