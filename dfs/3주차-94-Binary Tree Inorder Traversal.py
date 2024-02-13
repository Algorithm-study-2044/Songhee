# Q1. extend 를 쓰는 게 더 빠른가?
# Q2. 재귀 말고 반복문으로 표현하는 방법은 없는가?
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []