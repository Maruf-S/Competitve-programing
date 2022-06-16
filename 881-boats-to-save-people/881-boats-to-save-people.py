class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        res = 0
        while l <= r:
            bt = people[l] + people[r]
            if(bt <= limit):
                res += 1
                r -= 1
                l += 1
            elif r==l:
                res +=1 
                break
            else:
                res += 1
                r -= 1
        return res