from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root.left, root.right)])
        while q:
            l, r = q.popleft()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            q.append((l.left, r.right))
            q.append((l.right, r.left))
        return True

    # traversal로 풀면 안되는 이유: 반례 때문 -> 이걸 해결하기 전까지는 X
    def lr(self, root):
        return self.lr(root.left) + [root.val] + self.lr(root.right) if root else [-101]
    def rl(self, root):
        return self.rl(root.right) + [root.val] + self.rl(root.left) if root else [-101]
    def isSymmetric_traversal(self, root: Optional[TreeNode]) -> bool:
        l = self.lr(root.left)
        r = self.rl(root.right)
        
        if len(l) != len(r): return False
        for ll, rr in zip(l, r):
            if ll != rr: return False

        # root: [1,2,2,2,null,2]
        # print(l, r): [-101, 2, -101, 2, -101] [-101, 2, -101, 2, -101]
        return True