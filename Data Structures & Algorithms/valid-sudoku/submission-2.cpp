#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        bool rows[9][9] = {false};
        bool cols[9][9] = {false};
        bool boxes[9][9] = {false};

        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                char ch = board[r][c];
                if (ch == '.') continue;
                int v = ch - '1';
                int box = (r / 3) * 3 + (c / 3);

                if (rows[r][v] || cols[c][v] || boxes[box][v]) {
                    return false;
                }

                rows[r][v] = cols[c][v] = boxes[box][v] = true;
            }
        }
        return true;
    }
};