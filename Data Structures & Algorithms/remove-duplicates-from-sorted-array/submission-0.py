class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if i == n - 1 or num != nums[i + 1]:
                nums[insert] = num
                insert += 1
        return insert