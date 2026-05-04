class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        streak = 0
        for num in nums:
            streak = streak + 1 if num else 0
            best = max(best, streak)
        
        return best