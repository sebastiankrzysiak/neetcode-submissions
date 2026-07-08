class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])

        def is_valid(r, c):
            return 0 <= r < R and 0 <= c < C and grid[r][c] == "1"
        
        def visit(r, c):
            grid[r][c] = "0"
            for dir_r, dir_c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nxt_r = r + dir_r
                nxt_c = c + dir_c
                if is_valid(nxt_r, nxt_c):
                    visit(nxt_r, nxt_c)
        
        islands = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    visit(r, c)
                    islands += 1
        
        return islands
            
        
