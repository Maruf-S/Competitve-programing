class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        alpha = {j:i+1 for i,j in enumerate("abcdefghijklmnopqrstuvwxyz")}
        temp = 1
        # "x^0 x^1 x^2 x^3"
        # 1     7  49
        def getHash(string):
            nonlocal temp
            assert(len(string) == k)
            hash_val = 0
            for j,i in enumerate(string):
                hash_val+=(alpha[i] * temp)
                temp *= power
            return hash_val
        hash_val = getHash(s[:k])
        if hash_val%modulo == hashValue:
            return s[:k]
        for i in range(1,len(s) - k+1):
            hash_val = (hash_val - alpha[s[i-1]])
            hash_val += alpha[s[i + (k-1)]] * temp
            hash_val//=power
            # hash_val -= alpha[s[i-1]]
            # hash_val += (alpha[s[i+k-1]] * temp)
            # hash_val //= power
            if hash_val%modulo == hashValue:
                return s[i:i+k]
            