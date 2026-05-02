// lil bit
#include <vector>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int rows[9] = {0}, cols[9] = {0}, boxes[9] = {0};

        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                char ch = board[r][c];
                if (ch == '.') continue;

                int digit = ch - '1';
                int bit = 1 << digit;

                int box = (r / 3) * 3 + (c / 3);

                if (rows[r] & bit || cols[c] & bit || boxes[box] & bit) {
                    return false;
                }

                rows[r] |= bit;
                cols[c] |= bit;
                boxes[box] |= bit;
            }
        }
        return true;
    }
};