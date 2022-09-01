class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        if not digits:
            return []
        def dfs(idx,path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            for i in mapping[digits[idx]]:
                path.append(i)
                dfs(idx + 1,path)
                path.pop()
        dfs(0,[])
        return res