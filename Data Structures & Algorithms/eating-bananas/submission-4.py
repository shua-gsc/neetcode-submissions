class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def monke_can_eat_all_the_bananas(k: int) -> bool:
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / k)
            return total_hours <= h
            
        l, r = 1, max(piles)
        
        while l < r:
            mid = (l + r) // 2

            if monke_can_eat_all_the_bananas(mid):
                r = mid
            else:
                l = mid + 1
            
        return l