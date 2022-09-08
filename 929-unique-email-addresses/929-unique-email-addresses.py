class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        h = set()
        for i in emails:
            mail = ""
            flag = False
            for (k,j) in enumerate(i):
                if flag or j == "@":
                    if j == "@":
                        mail += i[k:]
                        break
                    continue
                if j == "+":
                    flag = True
                    continue
                if j == ".":
                    continue
                mail += j
            h.add(mail)
        print(h)
        return len(h)