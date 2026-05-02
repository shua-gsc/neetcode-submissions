# Simple version with Counter
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for n, count in freq.items():
            buckets[count].append(n)

        res = []
        for count in range(len(buckets) - 1, 0, -1):
            for n in buckets[count]:
                res.append(n)
                if len(res) == k:
                    return res