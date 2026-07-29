class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for c in s:
            if c.isalnum():
                ss += c
        l = 0
        r = len(ss) - 1
        while l < r:
            if not ss[l].isalnum():
                l += 1
            if not ss[r].isalnum():
                r -= 1
            if l < r and ss[l].lower() != ss[r].lower():
                return False
            l += 1
            r -= 1
        return True