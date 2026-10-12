impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut iter = strs.into_iter();

        let Some(mut prefix) = iter.next() else {
            return String::new();
        };

        for word in iter {
            let mut end = 0;
            for (a, b) in prefix.chars().zip(word.chars()) {
                if a != b {
                    break;
                }
                end += a.len_utf8();
            }
            prefix.truncate(end);
        }

        prefix
    }
}
