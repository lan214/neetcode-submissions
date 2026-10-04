from sortedcontainers import SortedDict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []

        res = list()
        seen = SortedDict()
        l = 0
        for r in range(len(nums)):
            num = nums[r]
            seen[num] = seen.get(num, 0) + 1
            if r - l + 1 == k:
                res.append(seen.peekitem(-1)[0])
                seen[nums[l]] -= 1
                if seen[nums[l]] == 0:
                    del seen[nums[l]]
                l += 1
        
        return res