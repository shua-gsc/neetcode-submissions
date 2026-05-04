class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let lo = 0;
        let hi = nums.length;

        do {
            const m = Math.floor(lo + (hi - lo) / 2);
            const v = nums[m];

            if (v === target)
                return m;
            if (v > target)
                hi = m;
            else
                lo = m + 1;
                
        } while (lo < hi);
        
        return -1;
    }
}