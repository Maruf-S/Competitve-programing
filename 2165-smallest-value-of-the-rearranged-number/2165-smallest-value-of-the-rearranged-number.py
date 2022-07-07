def comparer_function(a, b):
    if(int(a+b)>int(b+a)):
        return 1
    else:
        return -1
    return 0
from functools import cmp_to_key
class Solution:
    def smallestNumber(self, num: int) -> int:
        postive = num>0
        num = abs(num)
        cmp_key = cmp_to_key(comparer_function)
        digts = list(str(num))
        if postive:
            digts.sort()
            zero = 0
            for i,j in enumerate(digts):
                if j == "0":
                    zero+=1
                else:
                    return int(digts[i]+ "".join(["0"]*zero +digts[i+1:]))
        else:
            digts.sort(reverse=True)
            return int("-"+"".join(digts))