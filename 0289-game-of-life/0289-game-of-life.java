class Solution {
    public void gameOfLife(int[][] board) {
        int m = board.length, n = board[0].length;
        int[] directions = {-1, 0, 1};
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int liveNeighbors = 0;
                
                for (int x : directions) {
                    for (int y : directions) {
                        if (x == 0 && y == 0) continue;
                        int ni = i + x, nj = j + y;
                        if (ni >= 0 && ni < m && nj >= 0 && nj < n && (board[ni][nj] == 1 || board[ni][nj] == 2)) {
                            liveNeighbors++;
                        }
                    }
                }
                
                if (board[i][j] == 1) {
                    if (liveNeighbors < 2 || liveNeighbors > 3) {
                        board[i][j] = 2;
                    }
                } else if (board[i][j] == 0) {
                    if (liveNeighbors == 3) {
                        board[i][j] = -1;
                    }
                }
            }
        }
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 2) board[i][j] = 0;
                if (board[i][j] == -1) board[i][j] = 1;
            }
        }
    }
}