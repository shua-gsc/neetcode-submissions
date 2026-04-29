class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const pairs = {"(": ")", "{": "}", "[": "]"};
        let stack = [];

        for (const char of s) {
            if (pairs[char]) {
                stack.push(char);
            } else if (Object.values(pairs).includes(char)) {
                if (!stack.length || pairs[stack.pop()] !== char) {
                    return false;
                }
            }
        }
        return !stack.length;
    }
}
