class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        def dfs(i, subset):
            if i == n:
                res.append(list(subset))
                return
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1, subset)

        dfs(0, [])
        return res