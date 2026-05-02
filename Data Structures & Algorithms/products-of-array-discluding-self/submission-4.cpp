#include <vector>
using namespace std;

// Two linear passes but don't initialize out since we assign all anyway
// (my initial solution filled w/ 1s)

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = (int)nums.size();
        vector<int> out(n); // uninitialized

        int prefix = 1;
        for (int i = 0; i < n; ++i) {
            out[i] = prefix;
            prefix *= nums[i];
        }

        int rightProduct = 1;
        for (int i = n - 1; i >= 0; --i) {
            out[i] *= rightProduct;
            rightProduct *= nums[i];
        }
        return out;
    }

};

