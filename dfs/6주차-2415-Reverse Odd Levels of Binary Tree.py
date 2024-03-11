# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    d = defaultdict(list)
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 그냥 일반적으로 level 별로 child랑 grandchild를 바꿔주는 정도로는
        # level 전체의 reverse를 구현하기 어려움.
        # 따라서 2번의 traversal을 통해 구현한다!

        def search(x, depth=0):
            if not x:
                return
            self.d[depth].append(x.val) # default dict을 stack처럼 사용
            search(x.left, depth+1)
            search(x.right, depth+1)

        search(root)
        
        def dfs(x, depth=0):
            if not x:
                return
            if depth%2:
                x.val = self.d[depth].pop() # 역순으로 뽑아서 업데이트
            dfs(x.left, depth+1)
            dfs(x.right, depth+1)

        dfs(root)

        return root