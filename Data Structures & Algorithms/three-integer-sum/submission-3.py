class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        res = []
        for i in range(len(nums_sorted) - 2):
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
            l = i + 1
            r = len(nums_sorted) - 1
            while l < r:
                total =  nums_sorted[i] + nums_sorted[l] + nums_sorted[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums_sorted[i], nums_sorted[l], nums_sorted[r]])
                    l += 1
                    r -= 1
                    while l < r and nums_sorted[l-1] == nums_sorted[l]:
                        l += 1
        return res