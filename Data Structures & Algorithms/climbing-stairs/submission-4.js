class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        let a = 1, b = 1;
        for (let i = 0; i < n - 1; i++) {
            [a, b] = [b, b + a];
        }
        return b;
    }
}
