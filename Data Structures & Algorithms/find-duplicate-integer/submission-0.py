class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
