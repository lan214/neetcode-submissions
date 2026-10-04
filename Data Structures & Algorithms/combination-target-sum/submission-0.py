class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(target, i, combination):
            if target == 0:
                result.append(list(combination))
            if i >= len(nums) or target <= 0:
                return
            combination.append(nums[i])
            dfs(target - nums[i], i, combination)
            combination.pop()
            dfs(target, i + 1, combination)

        dfs(target, 0, [])
        return result