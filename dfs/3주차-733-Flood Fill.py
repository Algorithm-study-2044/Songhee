# [주의 & Q] if scolor != color 빼면 recursion error 뜸

#from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col, scolor = len(image), len(image[0]), image[sr][sc]
        def dfs(r, c):
            image[r][c] = color
            for (nr, nc) in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < row and 0 <= nc < col and image[nr][nc] == scolor:
                    dfs(nr, nc)
        if scolor != color:
            dfs(sr, sc)
        return image

    # bfs 방식: 시간 초과
    # def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    #     maxx, maxy = len(image), len(image[0])
    #     scolor = image[sr][sc]
    #     queue = deque([(sr, sc)])
    #     while queue:
    #         (x, y) = queue.popleft()
    #         for (dx, dy) in [(1,0),(0,1),(-1,0),(0,-1)]:
    #             nx, ny = x+dx, y+dy
    #             if nx < 0 or ny < 0 or nx >= maxx or ny >= maxy:
    #                 continue
    #             if image[nx][ny] == scolor:
    #                 queue.append((nx, ny))
    #                 image[nx][ny] = color
    #     return image

# 풀이 하나 더
class Solution(object):
    def fill(self, image, sr, sc, color, cur):
        # If sr is less than 0 or greater equals to the length of image...
        # Or, If sc is less than 0 or greater equals to the length of image[0]...
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]): return;
        # If image[sr][sc] is not equal to previous color...
        if cur != image[sr][sc]: return;
        # Update the image[sr][sc] as a color...
        image[sr][sc] = color;
        # Make four recursive calls to the function with (sr-1, sc), (sr+1, sc), (sr, sc-1) and (sr, sc+1)...
        self.fill(image, sr-1, sc, color, cur);
        self.fill(image, sr+1, sc, color, cur);
        self.fill(image, sr, sc-1, color, cur);
        self.fill(image, sr, sc+1, color, cur);
    def floodFill(self, image, sr, sc, color):
        # Avoid infinite loop if the new and old colors are the same...
        if image[sr][sc] == color: return image;
        # Run the fill function starting at the position given...
        self.fill(image, sr, sc, color, image[sr][sc]);
        return image;