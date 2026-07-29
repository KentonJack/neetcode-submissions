class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ls = set(nums)
        maxi = 1
        start = []
        for n in ls:
            if n - 1 not in ls:
                start.append(n)
        def iter(n, c):
            if n + 1 not in ls:
                return c
            return iter(n + 1, c + 1)
        for s in start:
            c = iter(s, 1)
            maxi = max(maxi, c)
        return maxi