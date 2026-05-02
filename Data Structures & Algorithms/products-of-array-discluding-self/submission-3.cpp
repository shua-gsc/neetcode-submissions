#include <vector>
using namespace std;

// Single loop verison updating prefix and suffix simulaneously
// -- still 2 multiplications per idx

// - Why it may be faster:
// 1 loop, fewer branches/loop-control overhead
// - Why it may be slower:
// Writes to `out` in two distance locations each iteration
// could be less cache-friendly than the two linear passes
// (depends on the cpu/cache)

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = (int)nums.size();
        vector<int> out(n, 1);

        int left{1}, right{1};
        for (int i = 0; i < n; ++i) {
            out[i] *= left;
            left *= nums[i];
            
            out[n - 1 - i] *= right;
            right *= nums[n - 1 - i];
        }

        return out;
    }

};

