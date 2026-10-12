impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut end = nums.len();
        let mut i = 0;
        while i < end {
            if nums[i] == val {
                nums.swap(i, end - 1);
                end -= 1;
            } else {
                i += 1;
            }
        }
        println!("{:?}", nums);
        end as i32
    }
}
