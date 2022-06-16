class Solution:
    def compress(self, chars: List[str]) -> int:
        slowBoi, fastBoi = 0, 0
        n = len(chars)
        while fastBoi < n:
            chars[slowBoi] = chars[fastBoi]
            count = 1
            while fastBoi + 1 < n and chars[fastBoi] == chars[fastBoi + 1]:
                fastBoi += 1
                count += 1
            if(count > 1):
                for c in str(count):
                    chars[slowBoi+1] = c
                    slowBoi+=1
            slowBoi+=1
            fastBoi+=1
        return slowBoi