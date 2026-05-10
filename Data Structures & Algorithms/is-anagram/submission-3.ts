class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string) {
        if (s.length !== t.length) {
            return false;
        }

        const count = new Array<number>(26).fill(0);

        for (const ch of s) {
            count[ch.charCodeAt(0) - 'a'.charCodeAt(0)]++;
        }

        for (const ch of t) {
            const i = ch.charCodeAt(0) - 'a'.charCodeAt(0);
            if (--count[i] < 0) {
                return false
            }
        }
        return true;
    }
}
