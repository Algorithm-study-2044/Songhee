# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMaxHeight(self, x, h=0):
        if not x:
            return h
        return max(self.findMaxHeight(x.left, h+1), self.findMaxHeight(x.right, h+1))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # 양쪽 서브트리의 max height 차이가 1 이하인 경우: height-balanced
        left = self.findMaxHeight(root.left)
        right = self.findMaxHeight(root.right)

        # 근데 이런 식으로 풀어버리면 시간이 오래 걸릴 수 있음.
        if abs(left-right) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

# 다른 사람 풀이
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs를 돌면서 balanced 여부와 max depth를 리스트로 저장하여 구현한다.
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = abs(left[1] - right[1]) <= 1 and left[0] and right[0]

            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
