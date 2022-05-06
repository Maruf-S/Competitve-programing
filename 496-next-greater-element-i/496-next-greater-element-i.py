class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = [-1]*len(nums1)
        d = {}
        for i in range(len(nums1)):
            d[nums1[i]] = i
        mono_stack = []

        for i in nums2:
            if i in d:
                while mono_stack and  mono_stack[-1]<i:
                    nxt_e = mono_stack.pop()
                    res[d[nxt_e]] = i
                mono_stack.append(i)
            else:
                while mono_stack and  mono_stack[-1]<i:
                    nxt_e = mono_stack.pop()
                    res[d[nxt_e]] = i
        return res