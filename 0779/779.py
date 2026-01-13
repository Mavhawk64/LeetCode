# Accepted: 04/26/2022
# Revised: 01/13/2026 -- Fixed return type (for some reason it was not accepted)
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        rep1 = "0110"
        rep2 = "1001"
        if n <= 3:
            return int((rep1 + rep2)[k - 1])
        s = rep1 + rep2
        parity = 0
        n -= 2
        ref = 2**n
        while ref >= 8:
            if ref < k:
                s = s[::-1]
                k -= ref
            n -= 1
            ref = 2**n
        return int(s[k - 1])
