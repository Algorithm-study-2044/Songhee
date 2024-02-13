# [주의] root를 거치는 길이 꼭 최대경로가 아닐 수 있다는 것에 유의하기 (!)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def depthOfNode(self, root, depth):
    #     if not root:
    #         return depth
    #     return max(self.depthOfNode(root.left, depth+1), self.depthOfNode(root.right, depth+1))

    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     # this path may not pass through the root (!)
    #     l = self.depthOfNode(root.left, 0)
    #     r = self.depthOfNode(root.right, 0)
    #     return l+r
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.diameter = max(self.diameter, left + right)

            return 1 + max(left,right)
        
        dfs(root)
        return self.diameter