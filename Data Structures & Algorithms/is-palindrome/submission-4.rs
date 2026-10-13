impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let s = s.as_bytes();
        let mut l = 0;
        let mut r = s.len() - 1;
        while l < r {
            if !s[l].is_ascii_alphanumeric() {
                l += 1;
            } else if !s[r].is_ascii_alphanumeric() {
                r -= 1;
            } else {
                if s[l].to_ascii_lowercase() != s[r].to_ascii_lowercase() {
                    return false;
                }
                l += 1;
                r -= 1;
            }
        }
        true
    }
}
