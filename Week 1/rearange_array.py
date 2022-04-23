def rearrangeArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    clear = False
    while(clear==False):
        clear = True
        for i in range(1,len(nums)-1):
            if(nums[i]==(nums[i-1]+nums[i+1])/2):
                nums[i-1],nums[i] = nums[i],nums[i-1]
                clear = False
    print(nums) 
    
rearrangeArray([3,4,0,2,5])
print([3,0,4,2,5])