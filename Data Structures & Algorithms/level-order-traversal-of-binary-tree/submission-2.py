class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [(root, 0)]
        bucket = [[]]
        if not root: return []
        while stack:
            node, count = stack.pop()
            if count == len(bucket):
                bucket.append([])
            bucket[count].append(node.val)
            if node.right:
                stack.append((node.right, count + 1))
            if node.left: 
                stack.append((node.left, count + 1))
        return bucket