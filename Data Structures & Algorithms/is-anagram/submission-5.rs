impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut count = [0; 26];

        for b in s.bytes() {
            count[(b - b'a') as usize] += 1;
        }

        for b in t.bytes() {
            let i = (b - b'a') as usize;
            count[i] -= 1;
            if count[i] < 0 {
                return false;
            }
        }
        return true;
    }
}
