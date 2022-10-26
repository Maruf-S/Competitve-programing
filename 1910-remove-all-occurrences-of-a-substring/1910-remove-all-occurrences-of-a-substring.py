"""
1. Find the substring 

2. Remove the substring
"""

class Solution:
    def find(self,s,target):
        """
        Returns the first occourance of a substring
        """
        if len(s) >= len(target):
            for i in range(len(s) - len(target) + 1):
                if s[i:i + len(target)] == target:
                    return i
        return -1
    def removeOccurrences(self, s: str, part: str) -> str:
        target_idx = self.find(s,part)
        while target_idx != -1:
            s = s[:target_idx] + s[target_idx + len(part):]
            target_idx = self.find(s,part)
        return s