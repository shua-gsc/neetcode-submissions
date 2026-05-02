class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bottom, top = 0, len(nums) - 1

        while bottom <= top:
            mid = (bottom + top) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                top = mid - 1
            else:
                bottom = mid + 1
        
        return -1
