class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Monacher's Algorithm
        sp = "#" + "#".join(list(s)) + "#"

        pr = [0 for i in sp]

        c = 0
        r = 0

        while c < len(sp):
            while c-(r+1) >= 0 and c+(r+1) < len(sp) and sp[c-(r+1)] == sp[c+(r+1)]:
                r += 1

            pr[c] = r
            
            co = c
            ro = r
            c += 1
            r = 0

            while c <= co + ro:
                mc = co - (c - co)
                mmr = co + ro - c
                if pr[mc] < mmr:
                    pr[c] = pr[mc]
                    c += 1
                   
                elif pr[mc] > mmr:
                    pr[c] = mmr
                    c += 1
                else:
                    r = mmr
                    break
        longest_r = max(pr)
        start = pr.index(longest_r) - longest_r
        end = pr.index(longest_r) + longest_r
        ret = "".join(sp[start:end+1].split("#"))
        return ret



print(Solution().longestPalindrome("mom"))
# print(Solution().longestPalindrome("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"))