class Solution(object):
    def sortColors(self,nums):
        n = len(nums)
        l_ptr = 0
        r_ptr = n-1
        i = 0
        while(i<=r_ptr):
            if(nums[i] == 0):
                nums[l_ptr],nums[i] = nums[i],nums[l_ptr]
                # Increment the left pointer aftter swapping
                l_ptr+=1
                i+=1
            elif(nums[i]==2):
                # Decrement the left pointer aftter swapping
                nums[i],nums[r_ptr] = nums[r_ptr],nums[i]
                r_ptr-=1
            else:
                #! You can't increment i after swaping with the right ptr or it'll skip over zeros onto the left
                i+=1
            print("I ==> " + str(i))
            print("R_Ptr ==> " + str(r_ptr))
            print("L_Ptr ==> " + str(l_ptr))
            