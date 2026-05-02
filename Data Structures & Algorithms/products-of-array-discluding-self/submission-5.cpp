#include <vector>
using namespace std;

// Pointer version cause why not
// ? Could reduce indexing overhead and help the compiler auto-vectorize
// **I believe multiplications are hard to vectorize due to loop-carried dependencies
// **I think modern compilers should be able to compile this similarly to the indexed version
// **I doubt this version would be faster, but it's a solution nonetheless

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = (int)nums.size();
        vector<int> out(n); 

        int prefix = 1;
        int* o = out.data();
        int* a = nums.data();

        for (int i = 0; i < n; ++i) {
            o[i] = prefix;
            prefix *= a[i];
        }

        int rightProduct = 1;
        for (int i = n - 1; i >= 0; --i) {
            out[i] *= rightProduct;
            rightProduct *= nums[i];
        }
        return out;
    }
};

