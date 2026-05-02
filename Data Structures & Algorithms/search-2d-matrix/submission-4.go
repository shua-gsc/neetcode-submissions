func searchMatrix(matrix [][]int, target int) bool {
    if len(matrix) == 0 || len(matrix[0]) == 0 {
        return false;
    }

    rows, cols := len(matrix), len(matrix[0])
    l, r := 0, rows * cols - 1

    for l <= r {
        mid := (l + r) / 2
        row := mid / cols
        col := mid - row * cols

        if matrix[row][col] == target {
            return true
        }
        if matrix[row][col] < target {
            l = mid + 1
        } else {
            r = mid - 1
        }
    }
    return false
}
