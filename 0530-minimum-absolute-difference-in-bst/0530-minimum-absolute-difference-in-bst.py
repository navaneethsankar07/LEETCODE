class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []

        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        
        inorder(root)
        min_diff = float('inf')

        for x in range(1,len(res)):
            min_diff = min(res[x] - res[x-1], min_diff)
        
        return min_diff