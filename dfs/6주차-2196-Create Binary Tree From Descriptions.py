# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        check = dict()
        parent = set()
        child = set()
        for desc in descriptions:
            p, c, isleft = desc
            if p not in check:
                check[p] = TreeNode(p)
            if c not in check:
                check[c] = TreeNode(c)
            parent.add(p)
            child.add(c)
            if isleft:
                check[p].left = check[c]
            else:
                check[p].right = check[c]
        root = list(parent - child)[0]
        return check[root]
        
            