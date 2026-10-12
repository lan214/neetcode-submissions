impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen: HashMap<i32, i32> = HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            let i = i as i32;
            let to_find = target - num;
            if seen.contains_key(&to_find) {
                return vec![seen[&to_find], i];
            }
            seen.insert(*num, i);
        }
        vec![-1,-1]
    }
}
