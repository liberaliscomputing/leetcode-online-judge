#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#Description
Count the number of prime numbers less than a non-negative number, n.

#Complexity
Time: O(2 * logn)
"""


class Solution(object):
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		isPrime = [0, 0] + [1 for i in range(2, n)]
		j = 2
		while j ** 2 < n:
			if isPrime[j]:
				k = 2
				while j * k < n:
					isPrime[j * k] = 0
					k += 1
			j += 1
		return sum(isPrime)

		"""
		#O(n^2): Time exceeded error
		result = 0
		for i in range(n):
			if self.isPrime(i):
				result += 1
		return result

		def isPrime(self, n):
			if n < 2:
				return False
			for i in range(2, n - 1):
				if n % i == 0:
					return False
			return True
		"""

if __name__ == '__main__':
	n = 10
	solution = Solution()
	print solution.countPrimes(n)

