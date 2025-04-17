class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
          
            left_gain = max(dfs(node.left), 0)  # Max path sum from left subtree
            right_gain = max(dfs(node.right), 0)  # Max path sum from right subtree
            
            price_newpath = node.val + left_gain + right_gain
            
            self.max_sum = max(self.max_sum, price_newpath)
            
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        
        return self.max_sum
