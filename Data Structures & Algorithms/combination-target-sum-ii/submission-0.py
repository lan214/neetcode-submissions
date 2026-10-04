class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        result = []
        n = len(nums)
        def dfs(target, i, combination):
            if target == 0:
                result.append(list(combination))
                return
            if i >= n or target < 0:
                return
            combination.append(nums[i])
            dfs(target - nums[i], i + 1, combination)
            combination.pop()
            j = i + 1
            while j < n and nums[j - 1] == nums[j]:
                j += 1
            dfs(target, j, combination)
        
        dfs(target, 0, [])
        return result