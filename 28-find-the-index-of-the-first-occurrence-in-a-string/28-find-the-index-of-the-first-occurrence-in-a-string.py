class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        MOD = (10 ** 9) + 7
        def getHash(s):
            assert(len(s) == len(needle))
            hash_val = 0
            k = len(s) - 1
            for i in range(len(s)):
                hash_val += (ord(s[i]) * (11 ** k))
                k -= 1
            return hash_val
        needle_hash = getHash(needle)
        if len(needle) > len(haystack):
            return -1
        window = getHash(haystack[:len(needle)])
        if window == needle_hash:
            return 0
        k = len(needle) 
        n = len(haystack)
        for i in range(1,n - k + 1):
            window -= (ord(haystack[i - 1]) * (11 ** (k - 1)))
            window *=11
            window += ord(haystack[i + k - 1]) 
            if window == needle_hash:
                return i
            
        return -1