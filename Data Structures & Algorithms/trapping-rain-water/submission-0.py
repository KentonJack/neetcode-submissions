class Solution:
    def trap(self, height: List[int]) -> int:
        pref = []
        suff = []
        cur = height[0]
        for i in range(len(height)):
            cur = max(cur, height[i])
            pref.append(cur)
        cur = height[-1]
        for i in range(len(height) - 1, -1, -1):
            cur = max(cur, height[i])
            suff.append(cur)
        suff.reverse()
        res = 0
        for i in range(len(height)):
            res += max(0, min(pref[i], suff[i]) - height[i])
        return res