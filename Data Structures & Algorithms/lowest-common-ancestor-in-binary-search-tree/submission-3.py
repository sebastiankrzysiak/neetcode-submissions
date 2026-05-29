# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root, target, path):
            if not root:
                return []

            path.append(root)

            if root.val == target.val:
                return path
            
            left = dfs(root.left, target, path)
            if left:
                return left
            
            right = dfs(root.right, target, path)
            if right:
                return right
            path.pop()
            
            return []
        
        path1 = dfs(root, p, [])
        path2 = dfs(root, q, [])

        i = 0
        while i < min(len(path1), len(path2)) and path1[i] == path2[i]:
            i += 1
        
        return path1[i - 1]