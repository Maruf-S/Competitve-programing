class Solution:
    def goodDaysToRobBank(self, sec: List[int], time: int) -> List[int]:
        n = len(sec)
        nonInc, nonDec = [0]*n, [0]*n
        
        for i in range(1,n):
            if sec[i-1]  >= sec[i]:
                nonInc[i] = nonInc[i-1]+1
        for i in range(n-2,0,-1):
            if sec[i] <= sec[i+1]:
                nonDec[i] = nonDec[i+1] + 1
        output = []
        print(nonInc)
        print(nonDec)
        for i in range(n):
            if nonInc[i] >= time and nonDec[i] >= time:
                output.append(i)
        return output