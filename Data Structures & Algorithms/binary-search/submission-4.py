class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)

        while lo < hi:
            m = lo + (hi - lo) // 2
            v = nums[m]
      
            if v == target:
                return m
        
            if v > target:
                hi = m
            else:
                lo = m + 1
    
        return -1

        