from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 1
        q = deque([(root, 1)])
        while q:
            x, d = q.popleft()
            if x.left:
                q.append((x.left, d+1))
                ans = d+1
            if x.right:
                q.append((x.right, d+1))
                ans = d+1
        return ans