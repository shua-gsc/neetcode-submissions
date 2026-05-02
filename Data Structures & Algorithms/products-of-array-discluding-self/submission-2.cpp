#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = (int)nums.size();
        vector<int> output(n, 1);

        int prefix = 1;
        for (int i = 0; i < n; ++i) {
            output[i] = prefix;
            prefix *= nums[i];
        }

        int rightProduct = 1;
        for (int i = n - 1; i >= 0; --i) {
            output[i] *= rightProduct;
            rightProduct *= nums[i];
        }

        return output;
    }
};