class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_consecutive = 0
        for num in nums:
            if num - 1 in num_set:
                continue
            current_num = num + 1
            while current_num in num_set:
                current_num += 1
            max_consecutive = max(max_consecutive, current_num - num)
        return max_consecutive