# 3주차-501-Find Mode in Binary Search Tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def findAllNodes(root):
            if not root:
                return []
            return [root.val] + findAllNodes(root.left) + findAllNodes(root.right)
        # mode = Counter(findAllNodes(root)).most_common(1) # mode가 여러 개일 때 고려하기
        def modeFinder(arr):
            c = Counter(arr)
            maxCnt = max(c.values())
            modes = []
            for val in c:
                if c[val] == maxCnt:
                    modes.append(val)
            return modes
        return modeFinder(findAllNodes(root))
        
# inorder traversal
# def inorder(self, root):
#     return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []
