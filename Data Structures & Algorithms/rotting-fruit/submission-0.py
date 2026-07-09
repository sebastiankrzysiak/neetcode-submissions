class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        def is_valid(r, c):
            return 0 <= r < R and 0 <= c < C and grid[r][c] == 1
        
        fresh = 0
        time = 0
        queue = deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        while queue:
            added = False
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dir_r, dir_c in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nxt_r = dir_r + r
                    nxt_c = dir_c + c
                    if is_valid(nxt_r, nxt_c):
                        added = True
                        grid[nxt_r][nxt_c] = 2
                        fresh -= 1
                        queue.append((nxt_r, nxt_c))
            if added:
                time += 1
        
        return time if fresh == 0 else -1
