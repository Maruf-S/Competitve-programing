class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        result = [True]*len(l)
        for i in range(len(l)):
            sub_arr = nums[l[i]:r[i]+1]
            sub_arr.sort()
            s_con = sub_arr[1]-sub_arr[0]
            j = 2
            while(j<len(sub_arr)):
                if(sub_arr[j]-sub_arr[j-1]!=s_con):
                    result[i] = False
                    break
                j+=1
        return result