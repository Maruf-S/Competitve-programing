# class Solution:
#     def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
#         s  = list(s)
#         def shift(c, k):
#             return chr(ord('a') + (26 + ord(c) - ord('a') + k) % 26)
#         sim = [0] * len(s)
#         for start,end,dirn in shifts:
#             for i in range(start,end + 1):
#                 sim[i] += (1 if dirn == 1 else -1)
#         res = []
#         for i,j in enumerate(sim):
#             res.append(shift(s[i],j))
#         return "".join(res)


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cum_shifts = [0 for _ in range(len(s)+1)]
        
        for st, end, d in shifts:
            if d == 0:
                cum_shifts[st] -= 1
                cum_shifts[end+1] += 1
            else:
                cum_shifts[st] += 1
                cum_shifts[end+1] -= 1
        print(cum_shifts)
        cum_sum = 0
        for i in range(len(s)):
            cum_sum += cum_shifts[i]
            
            new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97
            s = s[:i] + chr(new_code) + s[i+1:]
        
        return s