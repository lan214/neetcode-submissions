class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(i, current_set):
            if i == n:
                result.append(list(current_set))
                return
            current_set.append(nums[i])
            backtrack(i+1, current_set)
            current_set.pop()
            backtrack(i+1, current_set)
        
        backtrack(0, [])
        return result