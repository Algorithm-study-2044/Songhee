# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        depth = dict()
        parent = dict()

        def findDepth(x, d=0):
            depth[x.val] = d
            if x.left:
                findDepth(x.left, d+1)
                parent[x.left.val] = x
            if x.right:
                findDepth(x.right, d+1)
                parent[x.right.val] = x
        
        def findLCA(p, q):
            # depth 맞춰주기
            while depth[p.val] < depth[q.val]:
                q = parent[q.val]
            while depth[p.val] > depth[q.val]:
                p = parent[p.val]
            
            # lca 찾기
            while p.val != q.val:
                p = parent[p.val]
                q = parent[q.val]
            
            return p

        findDepth(root)
        return findLCA(p, q)
