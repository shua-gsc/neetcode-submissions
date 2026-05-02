class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const n = nums.length;
        const output = new Array(n).fill(1);

        // Prefix products: output[i] = product of nums[0..i)
        let prefix = 1;
        for (let i = 0; i < n; i++) {
            output[i] = prefix;
            prefix *= nums[i];
        }

        // Suffix products: multiply by product of nums(i..n)
        let rightProduct = 1;
        for (let i = n - 1; i >= 0; i--) {
            output[i] *= rightProduct;
            rightProduct *= nums[i];
        }

        return output;
    }
}
