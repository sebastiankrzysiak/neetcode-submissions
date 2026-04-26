class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        def is_valid(r, c):
            return 0 <= r < R and 0 <= c < C and grid[r][c] == 1
        
        maxArea = 0

        def visit(r, c):
            grid[r][c] = 0
            area = 1
            for dir_r, dir_c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nxt_r = r + dir_r
                nxt_c = c + dir_c
                if is_valid(nxt_r, nxt_c):
                    area += visit(nxt_r, nxt_c)
            
            return area
        
        for r in range(R):
            for c in range(C):
                if is_valid(r, c):
                    maxArea = max(maxArea, visit(r, c))
        
        return maxArea