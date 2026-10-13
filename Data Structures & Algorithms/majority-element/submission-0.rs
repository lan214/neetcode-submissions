impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut count: HashMap<i32, i32> = HashMap::new();
        let mut majority = nums[0];
        let mut majority_count = 1;
        for num in nums {
            *count.entry(num).or_insert(0) += 1;
            if majority_count < count[&num] {
                majority = num;
                majority_count = count[&num];
            }
        }
        majority
    }
}
