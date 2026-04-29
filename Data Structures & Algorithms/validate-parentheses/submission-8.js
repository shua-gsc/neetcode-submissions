class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        // And duh can't believe I didn't think of this sooner...
        if (s.length % 2 !== 0) { // false if odd
            return false;
        }
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
