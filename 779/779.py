# Accepted: 04/26/2022
class Solution:
	def kthGrammar(self, n: int, k: int) -> int:
		rep1 = '0110'
		rep2 = '1001'
		if n <= 3:
			return (rep1 + rep2)[k-1]
		s = rep1 + rep2
		parity = 0
		n -= 2
		ref = 2 ** n
		while ref >= 8:
			if ref < k:
				s = s[::-1]
				k -= ref
			n -= 1
			ref = 2 ** n
		return s[k-1]