class Solution:
    def isValid(self, s: str) -> bool:
        t = []
        pair = {"]":"[","}":"{",")":"("}
        for c in s:
            if c not in pair:
                t.append(c)
            elif len(t) == 0 or pair[c] != t[-1]:
                    return False
            else:
                t.pop()
        return len(t) == 0