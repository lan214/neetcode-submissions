impl Solution {
    pub fn valid_palindrome(s: String) -> bool {
        let s = s.as_bytes();

        fn is_palindrome(s: &[u8], mut l: usize, mut r: usize) -> bool {
            while l < r {
                if s[l] != s[r] {
                    return false;
                }
                l += 1;
                r -= 1;
            }
            true
        }

        let (mut l, mut r) = (0, s.len() - 1);
        while l < r {
            if s[l] != s[r] {
                return is_palindrome(s, l + 1, r)
                    || is_palindrome(s, l, r - 1);
            }
            l += 1;
            r -= 1;
        }

        true
    }
}