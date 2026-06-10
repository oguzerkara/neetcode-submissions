# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        stack = [(root, [root])]
        path_p, path_q = [], []

        while stack: 
            node, path = stack.pop()
            if node.val == p.val: path_p = path
            if node.val == q.val: path_q = path
            if path_p and path_q: break
            if node.left:
                stack.append((node.left, path + [node.left]))
            if node.right: 
                stack.append((node.right, path + [node.right]))
        i = 0
        lca = None
        while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
            lca = path_p[i]
            i += 1
        return lca