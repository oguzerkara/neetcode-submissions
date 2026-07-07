class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        def search(r, s):
            if not r and not s:
                return True
            if not r or not s:
                return False
            return (r.val == s.val and search(r.left, s.left) and search(r.right, s.right))
        if search(root, subRoot):
            return True
        return (self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot))