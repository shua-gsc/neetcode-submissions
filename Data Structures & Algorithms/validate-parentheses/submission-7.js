class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        // Better performance version than my previous solutions
        const pairs = {')': '(', '}': '{', ']': '['};
        const stack = [];

        for (let i = 0; i < s.length; i++) {
            const char = s[i];

            if (char === '(' || char === '{' || char === '[') {
                stack.push(char);
            } else {
                if (stack.pop() !== pairs[char]) {
                    return false;
                }
            }
        }
        return !stack.length;
    }
}
