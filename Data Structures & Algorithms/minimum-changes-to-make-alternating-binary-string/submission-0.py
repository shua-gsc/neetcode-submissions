class Solution:
    def minOperations(self, s: str) -> int:
        mismatches = sum(c != str(i % 2) for i, c in enumerate(s))
        return min (mismatches, len(s) - mismatches)