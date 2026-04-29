class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const bracketMap = {"(": ")", "{": "}", "[": "]"};
        let stack = [];

        for (const char of s) {
            if (bracketMap[char]) {
                stack.push(char);
            } else if (["}", "]", ")"].includes(char)) {
                if (!stack.length || bracketMap[stack.pop()] !== char) {
                    return false;
                }
            }
        }
        return stack.length === 0;
    }
}
