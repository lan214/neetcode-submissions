import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot_idx = self.partition(nums, left, right)

            if pivot_idx < k:
                left = pivot_idx + 1
            elif pivot_idx > k:
                right = pivot_idx - 1
            else:
                break
        
        return nums[k]

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def partition(self, nums: List[int], left: int, right: int) -> int:
        rand_idx = random.randint(left, right)
        self.swap(nums, right, rand_idx)
        pivot = nums[right]
        fill = left

        for i in range(left, right):
            if nums[i] < pivot:
                self.swap(nums, i, fill)
                fill += 1
        
        self.swap(nums, right, fill)
        return fill