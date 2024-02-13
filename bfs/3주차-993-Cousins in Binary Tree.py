from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xdepth, ydepth = 0, 0
        px, py = 0, 0 # not same parent!
        q = deque([(1, root, 0)])
        while q:
            p, node, d = q.popleft()
            if not node:
                continue
            if node.val == x:
                xdepth = d
                px = p
            if node.val == y:
                ydepth = d
                py = p
            q.append((node, node.left, d+1))
            q.append((node, node.right, d+1))
        return xdepth == ydepth and px != py