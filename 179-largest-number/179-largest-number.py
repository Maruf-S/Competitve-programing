def comparer_function(a, b):
    if(int(a+b)>int(b+a)):
        return 1
    else:
        return -1

class Solution(object):
    def largestNumber(self,nums):
        from functools import cmp_to_key
        """
        :type nums: List[int]
        :rtype: str
        """
        cmp_key = cmp_to_key(comparer_function)
        nums = list(map(str, nums))
        nums.sort(key=cmp_key, reverse=True)
        return str(int("".join(nums)))