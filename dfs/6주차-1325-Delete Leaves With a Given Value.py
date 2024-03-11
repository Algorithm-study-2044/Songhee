# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(x, target):
            if not x:
                return None
            # post-order traversal
            x.left = dfs(x.left, target)
            x.right = dfs(x.right, target)
            if not x.left and not x.right and x.val == target:
                return None
            return x
        
        return dfs(root, target)