class Solution:
    def maximum69Number (self, num: int) -> int:
        num = [i for i in str(num)]
        for i,j in enumerate(num):
            if j == "6":
                num[i] = "9"
                break
        return int("".join(num))