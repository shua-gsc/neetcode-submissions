class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        # suffix products, multiplied into output
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output
