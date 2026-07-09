class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return False
        def valid(node, low, high):
            if not node: return True
            if not (low < node.val < high): return False
            return True and valid(node.left, low, node.val) and valid(node.right, node.val, high)
        return True and valid(root, float("-inf"), float("inf"))