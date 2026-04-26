class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R = len(board)
        C = len(board[0])
        
        def is_valid(r, c):
            return 0 <= r < R and 0 <= c < C and board[r][c] == "O"
        
        def visit(r, c):
            board[r][c] = "T"
            for dir_r, dir_c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nxt_r = r + dir_r
                nxt_c = c + dir_c
                if is_valid(nxt_r, nxt_c):
                    visit(nxt_r, nxt_c)
        
        
        for r in range(R):
            if board[r][0] == "O":
                visit(r, 0)
            if board[r][C - 1] == "O":
                visit(r, C - 1)

        for c in range(C):
            if board[0][c] == "O":
                visit(0, c)
            if board[R - 1][c] == "O":
                visit(R - 1, c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"