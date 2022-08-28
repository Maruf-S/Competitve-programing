class Solution:
    def reconstructMatrix(self, upper, lower, colsum):
            ans = [[0]*len(colsum) for i in range(2)]
            for i,val in enumerate(colsum):
                if val==2:ans[0][i]=ans[1][i]=1;upper-=1;lower-=1
                elif val==1:
                    if upper>=lower:ans[0][i]=1;upper-=1
                    else:ans[1][i]=1;lower-=1           
            return ans if upper==lower==0 else []