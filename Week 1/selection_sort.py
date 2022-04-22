#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        pass
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            current_min = i
            for j in range(i+1,n):
                if(arr[j]<arr[current_min]):
                    current_min = j
            arr[i],arr[current_min] = arr[current_min],arr[i]
        return arr