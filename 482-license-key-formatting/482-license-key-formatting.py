class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        count = Counter(s)
        elepp = (len(s) - count["-"])//k
        res = ""
        l = 0
        for j,i in enumerate(s[::-1]):
            if i == "-":
                continue
            if l == k-1 and j!= len(s) - 1:
                res = "-" + i + res
                l = 0
            else:
                res = i + res
                l += 1
        return (res.strip("-"))