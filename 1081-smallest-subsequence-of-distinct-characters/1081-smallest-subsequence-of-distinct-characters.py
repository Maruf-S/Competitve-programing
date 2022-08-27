class Solution:
    def smallestSubsequence(self, s):
        last_occ = {c: i for i, c in enumerate(s)}
        stack = []
        Visited = set()
        
        for i, symbol in enumerate(s):
            if symbol in Visited: continue
            
            while (stack and symbol < stack[-1] and last_occ[stack[-1]] > i):
                Visited.remove(stack.pop())
           
            stack.append(symbol)
            Visited.add(symbol)        
        return "".join(stack)