class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        l, h = 0, rows * cols - 1

        while l <= h:
            mid = (l + h) // 2
            r, c = divmod(mid, cols)

            if matrix[r][c] == target:
                return True

            if matrix[r][c] > target:
                h = mid - 1
            else:
                l = mid + 1
        
        return False