# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def compare(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False

            left_b = compare(node1.left, node2.left)
            right_b = compare(node1.right, node2.right)

            if node1.val == node2.val:
                return (left_b and right_b and True)
            
            else:
                return (left_b and right_b and False)
        return compare(p,q)
            
                