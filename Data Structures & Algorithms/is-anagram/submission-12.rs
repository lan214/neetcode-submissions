impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut count = [0i32; 26];
        for c in s.bytes() {
            count[(c - b'a') as usize] += 1;
        }
        for c in t.bytes() {
            count[(c - b'a') as usize] -= 1;
        }
        count == [0i32; 26]
    }
}
