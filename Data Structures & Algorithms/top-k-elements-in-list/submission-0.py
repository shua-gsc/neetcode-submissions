class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # {n: count}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # buckets[freq] = [n]
        # len(buckets) is len(nums) + 1
        # so that buckets[len(nums)] is max index
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, count in freq.items():
            buckets[count].append(n)

        # iterate buckets in reverse order, return when len(res) reaches k
        res = []
        for count in range(len(buckets) - 1, 0, -1):
            for n in buckets[count]:
                res.append(n)
                if len(res) == k:
                    return res