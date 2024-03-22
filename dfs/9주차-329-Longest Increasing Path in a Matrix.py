# hard.. 
# 매 순간 dfs를 써야하고 update가 필요하다는 것
# dist[r][c]는 dp memorization, 가장 긴 루트의 길이를 저장
# cycle이 생기거나, 가로질러서 반복되는 현상은 생기지 않음 -> longest "increasing" path 라서.

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dist = defaultdict(int)
        
        def dfs(r, c):
            if (r, c) in dist:
                return dist[(r, c)]
            
            curr_dist = 1 # 기본 dist 값은 1 임에 유의.
            for (dr, dc) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if 0<=r+dr<len(matrix) and 0<=c+dc<len(matrix[0]) and matrix[r][c] < matrix[r+dr][c+dc]:
                    curr_dist = max(curr_dist, dfs(r+dr, c+dc)+1)
                    # 이렇게 되면 다 좋은데... cycle이 생기지 않을까? -> nope. 이유는 같은 걸 포함하지 않기 때문. 무조건 커지는 조합이라 cycle이나 가로지르는 현상 생기지 않음
            
            dist[(r, c)] = curr_dist
            return curr_dist

        ans = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ans = max(ans, dfs(r, c))

        return ans