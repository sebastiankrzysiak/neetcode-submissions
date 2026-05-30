# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        path = []
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            path.append(root.val)
            dfs(root.right)
        
        dfs(root)

        for i in range(1, len(path)):
            if not(path[i - 1] < path[i]):
                return False
        
        return True