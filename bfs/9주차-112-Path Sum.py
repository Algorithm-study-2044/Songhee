# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    leafsum = []

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(x, sum=0):
            if not x.left and not x.right:
                self.leafsum.append(sum+x.val)
                # print('leaf', x.val, self.leafsum)
            if x.left:
                dfs(x.left, sum+x.val)
            if x.right:
                dfs(x.right, sum+x.val)
        
        self.leafsum = []
        dfs(root)
        # print(self.leafsum)
        if targetSum in self.leafsum:
            return True
        return False
            
            