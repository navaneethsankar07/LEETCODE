# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0

        def recover(root):
            if root and root.right:
                root.right.val = 2 * root.val + 2
            if root and root.left:
                root.left.val = 2 * root.val + 1
            
            if root.left: recover(root.left)
            if root.right: recover(root.right)
        
        recover(self.root)
        self.vals = set()
        self.inorder(self.root, self.vals)
    
    def inorder(self, root, vals):
        if root:
            self.inorder(root.left, vals)
            vals.add(root.val)
            self.inorder(root.right, vals)

    def find(self, target: int) -> bool:
        return target in self.vals
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)