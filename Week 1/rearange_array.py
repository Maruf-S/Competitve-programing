def rearrangeArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range(1,len(nums)-1):
        if(nums[i]==(nums[i-1]+nums[i+1])/2):
            nums[i-1],nums[i] = nums[i],nums[i-1]
    print(nums) 
    
rearrangeArray([3,4,0,2,5])