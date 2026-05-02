class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean{
     */

    isValidSudoku(board) {
        const rows = Array(9).fill(0);
        const cols = Array(9).fill(0);
        const boxes = Array(9).fill(0);

        for (let r = 0; r < 9; r++) {
            for (let c = 0; c < 9; c++) {
                const v = board[r][c];
                if (v === ".") continue;

                const digit = v.charCodeAt(0) - 1;
                const bit = 1 << digit;

                const boxId = Math.floor(r / 3) * 3 + Math.floor(c / 3);

                if (rows[r] & bit) return false;
                if (cols[c] & bit) return false;
                if (boxes[boxId] & bit) return false;

                rows[r] |= bit;
                cols[c] |= bit;
                boxes[boxId] |= bit;
            }
        }
        return true;
    }
}