class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0, 0
            
            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)


            current_sum = node.val + left_sum + right_sum
            current_cnt = 1 + left_cnt + right_cnt

            if current_sum // current_cnt == node.val:
                self.ans += 1

            return current_sum, current_cnt
        
        dfs(root)
        return self.ans