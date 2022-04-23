def findOriginalArray(self, changed: List[int]) -> List[int]:
    out = []
    changed.sort()
    # for i in range(len(changed)):
    #     for j in range(i,len(changed)):
    #         if(changed[i]*2==changed[j]):
    #             out.append(changed[i])
    #             break
    i = 0
    while(i<len(changed)):
        for j in range(i,len(changed)):
            if(changed[i]*2==changed[j]):
                out.append(changed[i])
                changed.pop(i)
                break
        i+=1
    return out

x = findOriginalArray([1,3,4,2,6,8])
print(x)