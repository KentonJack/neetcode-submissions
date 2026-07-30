class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        maxi = 0
        c = defaultdict(int)
        for r in range(len(s)):
            c[s[r]] += 1
            maxi = max(maxi, c[s[r]])
            while r - l + 1 - maxi > k:
                c[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res