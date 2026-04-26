class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R = len(grid)
        C = len(grid[0])

        def is_valid(r, c):
            return 0 <= r < R and 0 <= c < C and grid[r][c] == 2**31 - 1

        distances = {(r, c) : 0 for r in range(R) for c in range(C) if grid[r][c] == 0}
        queue = deque([(r, c) for r in range(R) for c in range(C) if grid[r][c] == 0])

        while queue:
            r, c = queue.popleft()
            for dir_r, dir_c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nxt_r = r + dir_r
                nxt_c = c + dir_c
                if is_valid(nxt_r, nxt_c) and (nxt_r, nxt_c) not in distances:
                    distances[(nxt_r, nxt_c)] = distances[(r, c)] + 1
                    grid[nxt_r][nxt_c] = distances[(nxt_r, nxt_c)]
                    queue.append((nxt_r, nxt_c))