class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) {
            return false;
        }
        int rows = matrix.size(), cols = matrix[0].size();
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
};
