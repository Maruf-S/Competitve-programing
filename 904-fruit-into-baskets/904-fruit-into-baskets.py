class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = ans = 0
        basket = {}
        for i,j in enumerate(fruits):
            basket[j] = basket.get(j,0) + 1
            if len(basket)>2 :
                basket[fruits[l]] -= 1
                if(basket[fruits[l]]<=0):del basket[fruits[l]]
                l += 1
            ans = max(ans,i-l+1)
        return ans