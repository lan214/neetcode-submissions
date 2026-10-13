impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let s: Vec<char> = s.chars().collect();
        let mut l = 0 as usize;
        let mut r = s.len() - 1 as usize;
        while l < r {
            if !s[l].is_alphanumeric() {
                l += 1;
            } else if !s[r].is_alphanumeric() {
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
