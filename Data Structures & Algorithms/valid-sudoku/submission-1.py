class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R = len(board)
        C = len(board)

        for r in range(R):
            visited = set()
            for c in range(C):
                if board[r][c] == ".":
                    continue
                if board[r][c] in visited:
                    return False
                visited.add(board[r][c])

        for c in range(C):
            visited = set()
            for r in range(R):
                if board[r][c] == ".":
                    continue
                if board[r][c] in visited:
                    return False
                visited.add(board[r][c])
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                visited = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in visited:
                            return False
                        visited.add(board[r][c])
                        
        return True