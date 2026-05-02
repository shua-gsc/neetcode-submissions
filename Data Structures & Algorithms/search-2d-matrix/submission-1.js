class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        if (matrix.length === 0 || matrix[0].length === 0) {
            return false;
        }

        const rows = matrix.length, cols = matrix[0].length;
        let l = 0, r = rows * cols - 1;

        while (l <= r) {
            const mid = Math.floor((l + r) / 2);
            const row = Math.floor(mid / cols);
            const col = mid - row * cols;

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
