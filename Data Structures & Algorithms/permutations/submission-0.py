class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def dfs(nums, perm):
            if len(nums) == 0:
                result.append(list(perm))
            for i in range(len(nums)):
                dfs(nums[0:i]+nums[i+1:n], perm + [nums[i]])
        
        dfs(nums, [])
        return result