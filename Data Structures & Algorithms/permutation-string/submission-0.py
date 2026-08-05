class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1 = [0] * 26
        c2 = [0] * 26
        for c in s1:
            c1[ord(c) - ord('a')] += 1
        for i,c in enumerate(s2):
            c2[ord(c) - ord('a')] += 1
            if i >= len(s1):
                ch = s2[i - len(s1)]
                c2[ord(ch) - ord('a')] -= 1
            if c1 == c2:
                return True
        return False