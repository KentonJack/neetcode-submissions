class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for s in strs:
            e += f"{len(s)}#{s}"
        return e

    def decode(self, s: str) -> List[str]:
        d = []
        while s:
            ind = s.find('#')
            leng = int(s[:ind])
            s = s[ind + 1:]
            d.append(s[:leng])
            s = s[leng:]
        return d
