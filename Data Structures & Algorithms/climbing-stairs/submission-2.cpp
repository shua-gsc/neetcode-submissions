class Solution {
public:
    int climbStairs(int n) {
        int a, b;
        a = b = 1;
        for (int i = 0; i < n - 1; ++i) {
            a ^= b;
            b ^= a;
            a ^= b;
            b += a;
        }
        return b;
    }
};
