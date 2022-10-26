class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        MOD = (10 ** 9) + 7
        def getHash(s):
            assert(len(s) == len(needle))
            hash_val = 0
            k = len(s) - 1
            for i in range(len(s)):
                hash_val += ((ord(s[i]) * (31 ** k) % MOD)) % MOD
                k -= 1
            return hash_val % MOD
        needle_hash = getHash(needle) 
        if len(needle) > len(haystack):
            return -1
        window = getHash(haystack[:len(needle)])
        if window == needle_hash:
            return 0
        k = len(needle) 
        n = len(haystack)
        for i in range(1,n - k + 1):
            window -= (ord(haystack[i - 1]) * (31 ** (k - 1)) % MOD) % MOD
            window *=31
            window %= MOD
            window += ord(haystack[i + k - 1]) % MOD
            if window == needle_hash:
                return i
            
        return -1