impl Solution {
    pub fn valid_palindrome(s: String) -> bool {
        let s = s.as_bytes();
        return Self::is_palindrome(s, 1);
    }

    fn is_palindrome(s: &[u8], to_replace: u32) -> bool {
        let (mut l, mut r) = (0, s.len() - 1);
        while l < r {
            if !s[l].is_ascii_alphanumeric() {
                l += 1;
            } else if !s[r].is_ascii_alphanumeric() {
                r -= 1;
            } else {
                if s[l].to_ascii_lowercase() != s[r].to_ascii_lowercase() {
                    if to_replace == 0 {
                        return false;
                    }
                    return Self::is_palindrome(&s[l+1..=r], to_replace - 1) || Self::is_palindrome(&s[l..=r-1], to_replace - 1);
                }
                l += 1;
                r -= 1;
            }
        }
        return true;
    }
}
