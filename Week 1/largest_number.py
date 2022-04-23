def comparer_function(a, b):
    if(int(a+b)>int(b+a)):
        return 1
    else:
        return -1
    return 0


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
        out = ""
        significant_dig_entered = False

        for i in range(len(nums)-1):
            if(nums[i]=="0" and significant_dig_entered==False):
                continue
            else:
                out+=(nums[i])
                significant_dig_entered = True
        out+=(nums[-1])
        return out