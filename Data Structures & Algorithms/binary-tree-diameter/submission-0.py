class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        
        def get_depth(node):
            if not node:
                return 0
            
            left = get_depth(node.left)
            right = get_depth(node.right)
            
            # The diameter at this node is left height + right height
            self.max_len = max(self.max_len, left + right)
            
            # Return the height of this node to its parent
            return 1 + max(left, right)
            
        get_depth(root)
        return self.max_len