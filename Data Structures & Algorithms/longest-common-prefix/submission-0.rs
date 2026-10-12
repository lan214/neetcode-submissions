impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.len() == 0 {
            return String::new();
        }
        let mut res = strs[0].clone();
        for word in &strs[1..] {
            let mut common = String::new();
            for (a, b) in res.chars().zip(word.chars()) {
                if a == b {
                    common.push(a);
                } else {
                    break;
                }
            }
            res = common;
        }
        return res;
    }
}
