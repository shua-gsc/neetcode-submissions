class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        if (s.length % 2 !== 0) { 
            return false;
        }
        // Faster approach? push the closing bracket onto the stack
        const stack = [];

        for (let i = 0; i < s.length; i++) {
            const c = s[i];
            if (c === '(') stack.push(')');
            else if (c === '[') stack.push(']');
            else if (c === '{') stack.push('}');
            else if (stack.pop() !== c) return false;
        }
        return !stack.length;
    }
}
