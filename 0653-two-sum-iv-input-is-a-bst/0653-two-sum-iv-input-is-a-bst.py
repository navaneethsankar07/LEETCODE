# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = []

        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        
        inorder(root)
        left = 0
        right = len(res) -1 

        while left < right:
            val = res[left] + res[right]
            if val == k:
                return True
            elif val < k:
                left += 1
            
            else:
                right -= 1
        
        return False
        