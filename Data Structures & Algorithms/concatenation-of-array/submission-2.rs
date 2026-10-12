impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32>{
        let mut res: Vec<i32> = vec![];
        for _ in 0..2{
            for num in nums.iter() {
                res.push(*num);
            }
        }
        res
    }
}
