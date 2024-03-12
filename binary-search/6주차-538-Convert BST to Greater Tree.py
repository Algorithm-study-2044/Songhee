# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def trav(x):
            if not x:
                return []
            return trav(x.left) + [x.val] + trav(x.right)
        
        def change(x):
            if not x:
                return
            # root = [2,0,3,-4,1] 29/215 testcases passed (음수처리 관련, 지문을 제대로 읽자)
            x.val += sum([a for a in arr if a > x.val])
            change(x.left)
            change(x.right)

        # root=[] 7/215 testcases passed
        # root=[2] 28/215 testcases passed
        if not root or (not root.left and not root.right):
            return root

        arr = trav(root)
        change(root)
        return root