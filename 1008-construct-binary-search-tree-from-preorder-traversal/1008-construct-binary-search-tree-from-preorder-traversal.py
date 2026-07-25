# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        self.root = TreeNode(preorder[0])

        def insert(node, val):
            if node is None:
                return TreeNode(val)
            
            if val < node.val:
                node.left = insert(node.left, val)
            elif val > node.val:
                node.right = insert(node.right, val)
            
            return node
        
        for x in preorder[1:]:
            self.root = insert(self.root, x)
        return self.root
            
