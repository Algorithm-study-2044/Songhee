# 6주차-2415-Reverse Odd Levels of Binary Tree 이 문제랑 비슷한 느낌!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Use classical BFS algorithm, 
    # Find out left and right values at each root node and add it into queue, 
    # once you find childrens for root note, 
    # pick most recently added element to the queue 
    # which will be most right element.
    d = defaultdict(list)
    max_depth = 0

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def search(x, depth=0):
            if not x:
                return
            self.d[depth].append(x.val) # default dict을 stack처럼 사용
            search(x.left, depth+1)
            search(x.right, depth+1)
            self.max_depth = max(self.max_depth, depth+1)

        search(root)
        return [self.d[depth].pop() for depth in range(self.max_depth)]

# 다른 사람 풀이
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result: list[int] = []

        def dfs(node: Optional[TreeNode], level: int):
            nonlocal result # 중첩 함수 내 상위 함수 변수 사용할 때 이용.
            if not node:
                return

            # level이 증가할 때마다 
            if level >= len(result):
                result.append(node.val)

            # right 를 먼저 보는 방식을 택하므로서 bfs 방향이 오른쪽에서 왼쪽으로 향하고,
            # 오른쪽 첫 번째 노드를 항상 저장해서 결과적으로 right side view 가 가능해진다
            if node.right:
                dfs(node.right, level + 1)
            if node.left:
                dfs(node.left, level + 1)
            
        dfs(root, 0)
        return result