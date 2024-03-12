# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def trav(x):
            if not x:
                return []
            return trav(x.left) + [x.val] + trav(x.right)
        arr = trav(root)
        # [2,2,2] 53/85 testcases passed
        if len(arr) != len(set(arr)):
            return False
        arr2 = sorted(arr)
        for i, j in zip(arr, arr2):
            if i != j:
                return False
        return True

    # [5,4,6,null,null,3,7] 77/85 testcases passed
    # 올바르게 만들어졌다면 이럴 수 없음
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        elif not root.left and root.val < root.right.val:
            return self.isValidBST(root.right)
        elif not root.right and root.left.val < root.val:
            return self.isValidBST(root.left)
        elif root.left and root.right and root.left.val < root.val < root.right.val:
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False