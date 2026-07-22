# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        curr = TreeNode(-1)
        self.elements = []
        def inorder(root):
            if root:
                inorder(root.right)
                self.elements.append(root.val)
                inorder(root.left)
        
        inorder(root)
    def next(self) -> int:
        return self.elements.pop()
        
        

    def hasNext(self) -> bool:
        return len(self.elements) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()