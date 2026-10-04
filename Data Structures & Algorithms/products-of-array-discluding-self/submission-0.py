class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = nums.copy()
        right_product = nums.copy()
        for i in range(1, len(nums)):
            left_product[i] *= left_product[i-1]
            right_product[-1-i] *= right_product[-i]

        result = [1] * len(nums)
        result[0] = right_product[1]
        result[-1] = left_product[-2]

        for i in range(1, len(nums) - 1):
            result[i] = left_product[i-1] * right_product[i+1]
        
        return result