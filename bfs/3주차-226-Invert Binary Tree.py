from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = deque([root])
        while q:
            x = q.popleft()
            if not x:
                continue
            q.append(x.right)
            q.append(x.left)
            x.left, x.right = x.right, x.left
        return root