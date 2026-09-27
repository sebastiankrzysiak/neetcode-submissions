class Solution {
    private int R, C;
    private char[][] grid;

    public int numIslands(char[][] grid) {
        this.grid = grid;
        R = grid.length;
        C = grid[0].length;
        int result = 0;

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (grid[r][c] == '1') {
                    grid[r][c] = '0';
                    visit(r, c);
                    result++;
                }
            }
        }
        return result;
    }

    private boolean isValid(int r, int c) {
        return 0 <= r && r < R && 0 <= c && c < C && grid[r][c] == '1';
    }

    private void visit(int r, int c) {
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int i = 0; i < dirs.length; i++) {
            int nxtR = r + dirs[i][0];
            int nxtC = c + dirs[i][1];
            if (isValid(nxtR, nxtC)) {
                grid[nxtR][nxtC] = '0';
                visit(nxtR, nxtC);
            }
        }
    }
}
