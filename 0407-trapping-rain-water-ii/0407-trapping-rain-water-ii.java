class Solution {
    public int trapRainWater(int[][] heightMap) {
        int rowCount = heightMap.length, colCount = heightMap[0].length;
        boolean[][] isVisited = new boolean[rowCount][colCount];
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(cell -> cell[2]));

        for (int row = 0; row < rowCount; row++) {
            for (int col = 0; col < colCount; col++) {
                if (row == 0 || col == 0 || row == rowCount - 1 || col == colCount - 1) {
                    minHeap.offer(new int[] { row, col, heightMap[row][col] });
                    isVisited[row][col] = true;
                }
            }
        }

        int totalTrappedWater = 0;
        int[][] directions = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

        while (!minHeap.isEmpty()) {
            int[] currentCell = minHeap.poll();
            int currentRow = currentCell[0], currentCol = currentCell[1], currentHeight = currentCell[2];

            for (int[] direction : directions) {
                int newRow = currentRow + direction[0], newCol = currentCol + direction[1];

                if (newRow >= 0 && newRow < rowCount && newCol >= 0 && newCol < colCount
                        && !isVisited[newRow][newCol]) {
                    isVisited[newRow][newCol] = true;
                    int newHeight = heightMap[newRow][newCol];

                    totalTrappedWater += Math.max(0, currentHeight - newHeight);

                    minHeap.offer(new int[] { newRow, newCol, Math.max(newHeight, currentHeight) });
                }
            }
        }

        return totalTrappedWater;
    }
}