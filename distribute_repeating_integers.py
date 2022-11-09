class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:

        quantity.sort(reverse=True)
        freqCounts = Counter(Counter(nums).values())

        def helper(i):
            if i == len(quantity):
                return True
            
            for freq in list(freqCounts.keys()):
                count  = freqCounts[freq]
                if freq >= quantity[i] and count > 0:
                    # Use up the current
                    freqCounts[freq] -= 1
                    # Add what remains to the dict
                    freqCounts[freq - quantity[i]] += 1
                    if helper(i + 1):
                        return True
                    freqCounts[freq] += 1
                    freqCounts[freq - quantity[i]] -= 1
            
            return False
        
        return helper(0)
