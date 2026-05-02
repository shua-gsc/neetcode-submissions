public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        if (matrix.Length == 0 || matrix[0].Length == 0) {
            return false;
        }

        int rows = matrix.Length, cols = matrix[0].Length;
        int l = 0, r = rows * cols - 1;

        while (l <= r) {
            int mid = (l + r) / 2;
            int row = mid / cols;
            int col = mid - row * cols;

            if (matrix[row][col] == target) {
                return true;
            }

            if (matrix[row][col] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return false;
    }
}
